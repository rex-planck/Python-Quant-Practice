import os
from pathlib import Path

# === 配置项目名称 ===
PROJECT_NAME = "AShare_Macro_Rotation"

# === 定义量化项目的标准目录结构 ===
# 这种结构是买方机构常用的分层设计
STRUCTURE = {
    "data": ["raw", "processed"],          # 存放数据：raw(原始数据), processed(清洗后数据)
    "factors": ["alpha", "risk"],          # 因子挖掘：alpha(收益因子), risk(风险因子)
    "models": ["lgbm", "time_series"],     # 机器学习模型：lgbm(树模型), time_series(时序模型)
    "strategy": [],                        # 策略逻辑层
    "backtest": [],                        # 回测引擎与绩效分析
    "notebooks": [],                       # Jupyter 实验草稿区
    "config": [],                          # 配置文件 (如参数设置)
    "utils": []                            # 通用工具 (如日期处理、数据库连接)
}

def create_structure(base_path):
    root = Path(base_path) / PROJECT_NAME
    
    # 1. 创建根目录
    if not root.exists():
        root.mkdir(parents=True)
        print(f"✅ 项目根目录已创建: {root}")
    else:
        print(f"⚠️ 目录已存在: {root}")

    # 2. 创建子目录
    for folder, subfolders in STRUCTURE.items():
        # 创建一级子目录
        folder_path = root / folder
        folder_path.mkdir(exist_ok=True)
        # 创建 __init__.py 让其成为 Python Package
        (folder_path / "__init__.py").touch()
        
        # 创建二级子目录
        for sub in subfolders:
            sub_path = folder_path / sub
            sub_path.mkdir(exist_ok=True)
            (sub_path / "__init__.py").touch()

    # 3. 创建根目录下的入口文件
    (root / "main.py").touch()
    (root / "README.md").write_text(f"# {PROJECT_NAME}\n\n基于宏观状态识别的A股行业轮动系统", encoding='utf-8')
    (root / "requirements.txt").touch()

    print(f"\n🎉 量化工程架构初始化完成！")
    print(f"📂 位置: {root.absolute()}")

if __name__ == "__main__":
    # 获取当前脚本所在的文件夹
    current_dir = os.getcwd()
    create_structure(current_dir)