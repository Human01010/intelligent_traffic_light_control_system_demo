import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置随机种子以便结果可重复
np.random.seed(42)

# 生成数据的数量
num_samples = 1000

# 模拟车流量（假设在0到100之间）
car_flow = np.random.randint(0, 100, num_samples)

# 模拟人流量（假设在0到50之间）
pedestrian_flow = np.random.randint(0, 50, num_samples)

# 根据车流量和人流量生成信号灯时长
# 假设一个简单的规则：基础时长为20秒，每增加10辆车增加5秒，每增加10个行人增加2秒
signal_duration = 20 + (car_flow // 10) * 5 + (pedestrian_flow // 10) * 2

# 创建数据框
data = pd.DataFrame({
    'car_flow': car_flow,
    'pedestrian_flow': pedestrian_flow,
    'signal_duration': signal_duration
})

# 保存数据到CSV文件
data.to_csv('traffic_signal_data.csv', index=False)

# 输出前10条数据
print(data.head(10))

# 可视化数据分布
plt.figure(figsize=(10, 6))
plt.scatter(data['car_flow'], data['signal_duration'], c='blue', label='车流量 vs 信号灯时长', alpha=0.5)
plt.scatter(data['pedestrian_flow'], data['signal_duration'], c='red', label='人流量 vs 信号灯时长', alpha=0.5)
plt.xlabel('流量')
plt.ylabel('信号灯时长 (秒)')
plt.title('车流量和人流量与信号灯时长的关系')
plt.legend()
plt.grid(True)
plt.show()
