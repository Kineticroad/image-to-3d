---
title: Meshy Desktop BUILD 매뉴얼 초안
date: 2026-11-18
tags:
  - meshy
  - 빌드
  - 매뉴얼
target_file: BUILD.md
---

# Meshy Desktop BUILD 매뉴얼 초안

상위 노트: [[Meshy Desktop 개발 계획]]

> [!note] 용도
> 저장소의 `BUILD.md` 초안. Windows 정식 릴리스(12월) 전에 급한 사용자가 직접 실행하거나 빌드할 수 있도록 안내한다. README에서는 이 문서로 링크만 건다.

---

# 소스에서 직접 실행/빌드하기

## 0. 준비물
- Python 3.12 이상
- Git
- Meshy API 키: https://www.meshy.ai/developers/keys

## 1. 그냥 실행만 하기 (가장 빠름)

### macOS
```bash
git clone https://github.com/Kineticroad/image-to-3d.git
cd image-to-3d
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m meshy_desktop
```

### Windows (PowerShell)
```powershell
git clone https://github.com/Kineticroad/image-to-3d.git
cd image-to-3d
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m meshy_desktop
```

> Git이 없으면 GitHub Release 페이지의 **Source code (zip)**를 받아 압축을 풀어도 된다.

## 2. 실행 파일로 빌드하기
```bash
pip install pyinstaller
pyinstaller meshy-desktop.spec
```
→ `dist/` 폴더에 `.app`(macOS) 또는 `.exe`(Windows)가 생성된다.

## 3. 자주 나오는 문제
| 증상 | 해결 |
|---|---|
| macOS "확인되지 않은 개발자" 경고 | 앱 우클릭 → 열기 |
| Windows SmartScreen 경고 | 추가 정보 → 실행 |
| PowerShell 스크립트 실행 차단 | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `python` 명령을 못 찾음 (Windows) | Python 설치 시 "Add to PATH" 체크, 또는 `py` 사용 |
