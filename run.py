"""Launch AlphaPulse AI Paper Trader web application."""

import webbrowser
import threading
import uvicorn


def _open_browser():
    import time
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":
    print("=" * 60)
    print("  AlphaPulse AI 모의투자 플랫폼을 시작합니다...")
    print("  브라우저 접속 주소: http://127.0.0.1:8000")
    print("=" * 60)
    threading.Thread(target=_open_browser, daemon=True).start()
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False)
