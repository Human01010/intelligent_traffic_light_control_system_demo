import random
import time
import threading
from datetime import datetime
import requests
import json

# 1. 模拟传感器数据生成
def generate_mock_sensor_data(num_samples=10):
    """
    生成一组模拟的传感器数据，用于测试交通信号灯控制系统。
    :param num_samples: 生成的数据样本数量
    :return: 包含模拟数据的列表
    """
    data_samples = []
    for _ in range(num_samples):
        data = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),  # 当前时间戳
            'traffic_volume': random.randint(50, 300),  # 随机生成交通流量（单位：车辆数）
            'vehicle_speeds': [random.randint(20, 120) for _ in range(random.randint(5, 20))],  # 随机生成车辆速度（单位：km/h）
            'pedestrian_count': random.randint(0, 50),  # 随机生成行人数目
            'traffic_light_state': random.choice(['RED', 'GREEN', 'YELLOW'])  # 随机生成当前信号灯状态
        }
        data_samples.append(data)
    return data_samples

# 生成并打印模拟数据
print("Generated Mock Sensor Data Samples:")
mock_data_samples = generate_mock_sensor_data()
for i, sample in enumerate(mock_data_samples):
    print(f"Sample {i + 1}: {sample}")

# 2. 网络传输 - 模拟数据发送到服务器
def send_data_to_server(data):
    """
    将模拟数据发送到服务器。
    :param data: 模拟的传感器数据
    :return: HTTP响应状态码
    """
    server_url = "http://localhost:5000/traffic_data"  # 假设服务器地址
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(server_url, data=json.dumps(data), headers=headers)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to server: {e}")
        return None

# 模拟数据传输
print("\nSimulated Data Transmission to Server:")
sensor_data = generate_mock_sensor_data(1)[0]  # 生成一条模拟数据
print(send_data_to_server(sensor_data))

# 3. 信号灯时间计算 - 基于流量和行人数量
def calculate_signal_time(traffic_volume, pedestrian_count):
    """
    根据交通流量和行人数量计算信号灯的时间。
    :param traffic_volume: 交通流量（车辆数）
    :param pedestrian_count: 行人数目
    :return: 计算的信号灯时间（秒）
    """
    base_time = 30  # 基础信号时间
    additional_time = traffic_volume / 10  # 基于交通流量增加时间
    if pedestrian_count > 10:
        additional_time += 10  # 如果行人数目超过10，增加时间
    return base_time + additional_time

# 决策算法示例
print("\nSignal Timing Calculation Example:")
sensor_data = generate_mock_sensor_data(1)[0]  # 生成一条模拟数据
signal_time = calculate_signal_time(sensor_data['traffic_volume'], sensor_data['pedestrian_count'])
print(f"Next signal time: {signal_time} seconds")

# 4. 信号灯控制
class TrafficLightController:
    def __init__(self):
        self.current_light = "RED"
        self.stop_event = threading.Event()  # 用于控制线程的停止

    def change_light(self, next_light):
        """
        改变信号灯的状态。
        :param next_light: 下一个信号灯的状态（RED, GREEN, YELLOW）
        """
        self.current_light = next_light
        print(f"Signal changed to: {self.current_light}")

    def run(self):
        """
        开始运行信号灯控制系统。
        """
        while not self.stop_event.is_set():  # 使用事件来控制循环
            # 获取传感器数据并计算下一个信号灯时间
            sensor_data = generate_mock_sensor_data(1)[0]  # 生成一条模拟数据
            next_signal_time = calculate_signal_time(sensor_data['traffic_volume'], sensor_data['pedestrian_count'])

            # 改变信号灯
            self.change_light("GREEN")
            time.sleep(next_signal_time)  # 保持绿灯
            self.change_light("RED")
            time.sleep(5)  # 红灯保持5秒

    def stop(self):
        """
        停止信号灯控制系统。
        """
        self.stop_event.set()  # 触发停止事件

# 运行信号灯控制系统
print("\nTraffic Light Control System Running:")
controller = TrafficLightController()
light_control_thread = threading.Thread(target=controller.run)
light_control_thread.start()

# 假设我们想在10秒后停止信号灯控制
time.sleep(10)
controller.stop()
light_control_thread.join()  # 等待线程优雅退出
print("Traffic Light Control System Stopped.")
