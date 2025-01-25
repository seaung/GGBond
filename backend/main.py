import os
import sys
import logging
import uvicorn
from typing import Any
from app import create_app
from app.configs.config import settings

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def init_app() -> Any:
    """初始化应用
    包括环境检查、数据库连接测试等
    """
    try:
        app = create_app()
        # TODO: 在这里添加其他初始化检查
        return app
    except Exception as e:
        logger.error(f"应用初始化失败: {str(e)}")
        sys.exit(1)

app = init_app()

if __name__ == "__main__":
    # 获取环境变量或使用默认值
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "9527"))
    workers = int(os.getenv("APP_WORKERS", "4"))
    
    # 配置uvicorn运行参数
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        workers=workers,
        reload=settings.DEBUG,  # 开发环境启用热重载
        log_level="info",
        access_log=True
    )

