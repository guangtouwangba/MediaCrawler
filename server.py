from enum import Enum

from pydantic import BaseModel

import config
from main import CrawlerFactory
from recv_sms import app


class SearchType(Enum):
    XHS = "xhs"
    DOUYIN = ""


class SearchRequest(BaseModel):
    platform: str
    login_type: str
    type : str
    start: int
    keywords: str


@app.post("/search")
async def search_xsh(search_request: SearchRequest):
    config.PLATFORM = search_request.platform
    config.LOGIN_TYPE = search_request.login_type
    config.CRAWLER_TYPE = search_request.type
    config.START_PAGE = search_request.start
    config.KEYWORDS = search_request.keywords
    crawler = CrawlerFactory.create_crawler(platform=config.PLATFORM)
    await crawler.start()
    return {"status": "ok"}



