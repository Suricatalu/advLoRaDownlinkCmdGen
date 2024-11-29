# main.py
import shared.downlinkFields as DWHDR
from products.WISE2410 import WISE2410

def wise2410testfft():
    # 创建 WISE2410 设备实例
    device = WISE2410()
    
    # 设置参数
    fft_type = DWHDR.FFT_TYPE_LT  # FFT 指令类型，假设在 downlinkFields 中定义
    fcnt = 0                      # 帧计数器
    log_index = 55                # 日志索引
    timestamp = 1729841700        # 时间戳
    isX = True                    # 包含 X 轴数据
    isY = True                    # 包含 Y 轴数据
    isZ = True                    # 包含 Z 轴数据
    version = 0                   # 指令版本

    # 生成 FFT 指令
    command = device.gen_fft_command(
        type=fft_type,
        fcnt=fcnt,
        log_index=log_index,
        timestamp=timestamp,
        isX=isX,
        isY=isY,
        isZ=isZ,
        version=version
    )

    # 打印生成的指令
    print(f"Generated WISE-2410 FFT Command: {command}")

def wise2410testtimesync():
    device = WISE2410()

    cmd = device.time_sync(
        type = DWHDR.TIMESYNC_TYPE_I,
        fcnt = 0,
        timestamp = "2020-06-23T10:16:07+08:00",
        version = 0
    )

    print(f"Generated WISE-2410 Command: {cmd}")

def main():
    wise2410testtimesync()

if __name__ == "__main__":
    main()