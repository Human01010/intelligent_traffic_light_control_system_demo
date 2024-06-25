import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. 数据采集 - 模拟传感器数据
# 假设每秒钟采集一次车流量和人流量数据
def collect_data():
    car_flow = np.random.randint(0, 100)  # 车流量
    pedestrian_flow = np.random.randint(0, 50)  # 人流量
    return car_flow, pedestrian_flow

# 2. 数据传输 - 模拟数据传输到本地服务器
def transmit_data(data):
    # 使用5G网络传输数据
    # 模拟过程,直接返回数据
    return data

# 3. 数据处理与存储 - 存储在DataFrame中
data_store = pd.DataFrame(columns=['car_flow', 'pedestrian_flow', 'signal_duration'])

# 采集并传输1000次数据
for _ in range(1000):
    car_flow, pedestrian_flow = collect_data()
    transmitted_data = transmit_data((car_flow, pedestrian_flow))
    signal_duration = 30  # 初始信号灯时长
    data_store = data_store.append({
        'car_flow': transmitted_data[0],
        'pedestrian_flow': transmitted_data[1],
        'signal_duration': signal_duration
    }, ignore_index=True)

# 4. 模型训练与预测
# 假设我们有一些历史数据来训练模型，这里使用生成的数据
X = data_store[['car_flow', 'pedestrian_flow']]
y = data_store['signal_duration']

# 标准化数据
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 训练Logistic回归模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 模型评估
accuracy = accuracy_score(y_test, y_pred)
print(f"模型准确性: {accuracy * 100:.2f}%")

# 5. 实时交通信号灯控制
def control_traffic_signal(car_flow, pedestrian_flow):
    # 使用训练好的模型预测信号灯时长
    input_data = scaler.transform([[car_flow, pedestrian_flow]])
    predicted_duration = model.predict(input_data)
    return predicted_duration[0]

# 模拟实时数据控制
for _ in range(10):
    car_flow, pedestrian_flow = collect_data()
    optimal_duration = control_traffic_signal(car_flow, pedestrian_flow)
    print(f"车流量: {car_flow}, 人流量: {pedestrian_flow}, 建议信号灯时长: {optimal_duration} 秒")

# 6. 接口集成
# 此处假设有一个简单的接口函数，将预测结果发送到交通控制中心和导航系统
def integrate_with_control_center(duration):
    print(f"发送到交通控制中心的信号灯时长: {duration} 秒")

for _ in range(10):
    car_flow, pedestrian_flow = collect_data()
    optimal_duration = control_traffic_signal(car_flow, pedestrian_flow)
    integrate_with_control_center(optimal_duration)
