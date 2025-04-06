import asyncio
import httpx

async def test_server():
    async with httpx.AsyncClient() as client:
        # 1. 상태 확인
        health = await client.get("http://localhost:8000/health")
        print("서버 상태:", health.json())

        # 2. 채팅 테스트
        chat = await client.post(
            "http://localhost:8000/api/chat",
            json={
                "message": "안녕하세요!",
                "context_id": null
            }
        )
        print("채팅 응답:", chat.json())

# 실행
asyncio.run(test_server())