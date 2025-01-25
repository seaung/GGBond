from typing import Any, Optional, Dict, List, Union
from fastapi.responses import JSONResponse
from fastapi import status


class ResponseModel:
    """统一的HTTP响应封装类"""
    def __init__(
        self,
        code: int = status.HTTP_200_OK,
        msg: str = "ok",
        data: Optional[Any] = None
    ) -> None:
        self.code = code
        self.msg = msg
        self.data = data

    def dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        response = {
            "code": self.code,
            "msg": self.msg
        }
        if self.data is not None:
            response["data"] = self.data
        return response

    def json_response(self) -> JSONResponse:
        """转换为FastAPI的JSONResponse"""
        return JSONResponse(content=self.dict())

    @classmethod
    def success(cls, data: Optional[Any] = None, msg: str = "ok") -> "ResponseModel":
        """成功响应"""
        return cls(code=status.HTTP_200_OK, msg=msg, data=data)

    @classmethod
    def error(cls, msg: str = "error", code: int = status.HTTP_400_BAD_REQUEST) -> "ResponseModel":
        """错误响应"""
        return cls(code=code, msg=msg)

    @classmethod
    def paginate(
        cls,
        items: List[Any],
        total: int,
        page: int,
        page_size: int
    ) -> "ResponseModel":
        """分页数据响应"""
        return cls.success(data={
            "items": items,
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": (total + page_size - 1) // page_size
        })

    @classmethod
    def forbidden(cls, msg: str = "权限不足") -> "ResponseModel":
        """权限不足响应"""
        return cls.error(msg=msg, code=status.HTTP_403_FORBIDDEN)

    @classmethod
    def not_found(cls, msg: str = "资源不存在") -> "ResponseModel":
        """资源不存在响应"""
        return cls.error(msg=msg, code=status.HTTP_404_NOT_FOUND)

    @classmethod
    def validation_error(cls, msg: str = "参数验证错误") -> "ResponseModel":
        """参数验证错误响应"""
        return cls.error(msg=msg, code=status.HTTP_422_UNPROCESSABLE_ENTITY)