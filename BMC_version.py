import subprocess

def get_bmc_version():
    try:
        # 執行 ipmitool 命令以獲取 BMC 版本
        result = subprocess.run(['ipmitool', 'mc', 'info'], capture_output=True, text=True, check=True)
        
        # 解析命令輸出
        output = result.stdout
        for line in output.splitlines():
            if "Firmware Revision" in line:
                # 提取並返回固件版本
                return line.split(":")[1].strip()
        
        return "BMC version not found"
    
    except subprocess.CalledProcessError as e:
        return f"Error executing ipmitool: {e}"

# 執行並打印 BMC 版本
bmc_version = get_bmc_version()
print("BMC Version:", bmc_version)
