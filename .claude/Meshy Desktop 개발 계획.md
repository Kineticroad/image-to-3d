---
title: Meshy Desktop 개발 계획
date: 2026-11-18
status: 기획
tags:
  - 프로젝트
  - python
  - pyside6
  - meshy
  - 오픈소스
  - 개발일지
platform:
  - macOS (v0.1.0, 2026-11)
  - Windows (v0.2.0, 2026-12)
license: MIT
---

# Meshy Desktop 개발 계획

> [!summary] 한 줄 요약
> 이미지를 올리면 Meshy AI API로 3D 모델을 만들어 주는 **Python GUI 데스크톱 앱**.
> GitHub에 오픈소스로 공개하고, 개발 과정을 블로그 개발일지로 연재한다.

관련 노트: [[Meshy API 참고 문서]] · [[Meshy Desktop 블로그 연재 계획]] · [[Meshy Desktop BUILD 매뉴얼 초안]]

---

## 1. 요구사항

1. **Python**으로 작성: Mac/Windows 모두 지원
2. **GUI**: 일반 사용자도 쉽게 사용
3. **Meshy AI Image to 3D API** 연동
4. **GitHub 오픈소스** 공개 + **GitHub Release**로 실행 파일 배포
5. 단계별 **블로그 개발일지** 작성
6. 각 API 연동마다 **Meshy Docs 참고 링크**를 남긴다
7. 당장은 **macOS만** 배포하고, **Windows는 12월** 귀국 후 업데이트
8. 급한 Windows 사용자용 **소스 빌드 매뉴얼** 제공

---

## 2. 먼저 짚을 점

> [!warning] PyInstaller는 크로스 컴파일이 안 된다
> Mac에서 Windows `.exe`를 만들 수 없다. Windows 빌드는 Windows에서 하거나 **GitHub Actions의 `windows-latest` 러너**를 사용한다.

> [!warning] 결과물 보관 기간 3일
> Meshy는 Enterprise가 아닌 고객의 생성 결과물을 **최대 3일**만 보관한다. 작업이 끝나면 앱이 **자동으로 다운로드**하도록 구현한다.

> [!info] 크레딧
> - 텍스처가 있는 Image to 3D는 작업 하나에 **30크레딧**이고, 작업을 만들 때 차감된다. FAILED 작업만 환불된다.
> - 잔액 조회(`GET /openapi/v1/balance`)는 0크레딧이므로 UI에 잔액을 표시한다.
> - 개발 중에는 테스트 이미지를 최소한으로 사용한다.

> [!danger] API 키는 절대 커밋 금지
> 사용자가 각자 키를 입력하고, 앱은 `keyring`으로 OS 보안 저장소(macOS 키체인 / Windows 자격 증명 관리자)에 보관한다.

---

## 3. 기술 스택

| 영역    | 선택                                    | 이유                               |
| ----- | ------------------------------------- | -------------------------------- |
| 언어    | Python 3.12                           | 요구사항                             |
| GUI   | **PySide6 (Qt)**                      | 네이티브에 가까운 UI, LGPL이라 오픈소스 배포가 편함 |
| HTTP  | `httpx`                               | 타임아웃·재시도 처리가 쉬움                  |
| 키 저장  | `keyring`                             | OS 보안 저장소 사용                     |
| 패키징   | PyInstaller                           | `.app` / `.exe`                  |
| CI/CD | GitHub Actions                        | OS별 빌드와 Release 업로드 자동화          |
| 의존성   | `venv` + `requirements.txt` (또는 `uv`) | 블로그 독자도 따라 하기 쉬움                 |

---

## 4. Meshy API 흐름 (앱의 핵심)

1. **업로드**: 로컬 이미지를 **base64 data URI**로 변환해 보낸다. JPG·PNG·WebP, 20MB 이하라 별도 호스팅이 필요 없다.
2. **작업 생성**: `POST /openapi/v1/image-to-3d`를 호출하면 `result`에 task_id가 돌아온다.
3. **진행률**: `GET /openapi/v1/image-to-3d/:id`로 폴링하거나 `/stream`(SSE)을 사용한다.
   - `status`: `PENDING` → `IN_PROGRESS` → `SUCCEEDED` / `FAILED` / `CANCELED`
   - `progress`(0~100)는 GUI 진행 바에 연결한다.
4. **다운로드**: `model_urls`(glb, fbx, obj, usdz, stl)와 `thumbnail_url`을 받는다.
5. **옵션 노출**: 기본 화면에는 `target_formats`, 텍스처 on/off, PBR만 두고 나머지는 "고급 설정"으로 보낸다.

> [!tip] GUI 멈춤 방지
> 네트워크 작업은 반드시 `QThread` 같은 **백그라운드 워커**에서 실행한다.

자세한 문서 링크: [[Meshy API 참고 문서]]

---

## 5. 프로젝트 구조

```
meshy-desktop/
├── src/meshy_desktop/
│   ├── __main__.py          # python -m meshy_desktop
│   ├── main.py              # 진입점
│   ├── api/client.py        # Meshy API 래퍼 (GUI와 분리)
│   ├── core/worker.py       # QThread 백그라운드 작업
│   ├── core/settings.py     # keyring, 설정 저장
│   └── ui/                  # 메인 윈도우, 설정 창, 위젯
├── tests/                   # API 클라이언트 mock 테스트
├── assets/icons/            # .icns(Mac), .ico(Win)
├── docs/
│   └── API_REFERENCES.md    # 기능별 Meshy Docs 링크 표
├── .github/workflows/build.yml
├── meshy-desktop.spec       # PyInstaller 설정
├── pyproject.toml
├── requirements.txt
├── README.md / README.ko.md
├── BUILD.md                 # 소스에서 직접 실행/빌드하기
├── CHANGELOG.md
├── LICENSE                  # MIT
└── .gitignore               # .env, dist/, build/, .venv/
```

---

## 6. 릴리스 전략

| 시점 | 버전 | Release 첨부 파일 | 비고 |
|---|---|---|---|
| 2026-11 (출장 중) | `v0.1.0` | `MeshyDesktop-macOS-arm64.zip` | Windows 사용자는 [[Meshy Desktop BUILD 매뉴얼 초안\|BUILD.md]] 안내 |
| 2026-12 (귀국 후) | `v0.2.0` | Mac zip + `MeshyDesktop-Windows-x64.zip` | Windows 실기 테스트 후 공개 |

- GitHub Release에는 **Source code (zip / tar.gz)**가 자동으로 첨부된다. 급한 사용자는 여기서 소스를 받으면 된다.
- GitHub Actions는 지금은 **macOS만** 켜 둔다. 12월에는 matrix에 `windows-latest`를 추가한다.
- `v*` 태그를 푸시하면 빌드 결과가 Release에 자동 업로드되도록 한다.
- `macos-latest` 러너는 Apple Silicon(arm64) 빌드를 만든다. Intel Mac은 필요할 때 따로 대응한다.

---

## 7. 단계별 로드맵

### 2026-11 (macOS)
- [ ] **0. 기획**: MVP 범위 확정, Meshy 계정·API 키 발급 → 블로그 #1
- [ ] **1. 환경 세팅**: GitHub 저장소 생성, venv, `.gitignore`·LICENSE·README 뼈대, 첫 커밋 → 블로그 #2
- [ ] **2. API 검증 (CLI)**: 스크립트로 업로드 → 폴링 → `.glb` 다운로드 성공 → 블로그 #3
- [ ] **3. API 클라이언트 모듈화**: `client.py`, 401·429·FAILED 처리, 재시도, mock 테스트 → 블로그 #4
- [ ] **4. GUI 기본**: 드래그앤드롭, 이미지 미리보기, 변환 버튼, 진행 바 → 블로그 #5
- [ ] **5. 사용성**: API 키 설정(keyring), 포맷 선택, 저장 폴더, 잔액 표시, 작업 히스토리 → 블로그 #6
- [ ] **6. 패키징 (로컬)**: PyInstaller `.app`, 아이콘 적용 → 블로그 #7
- [ ] **7. CI/CD + v0.1.0**: Actions(macOS), `BUILD.md`, `docs/API_REFERENCES.md`, Release → 블로그 #8

### 2026-12 (Windows)
- [ ] **8. Windows 대응**: 실기 테스트, 경로·폰트 같은 OS 차이 수정, `.ico` 적용 → 블로그 #9
- [ ] **9. CI matrix 확장 + v0.2.0**: `windows-latest` 추가, Release → 블로그 #10 (회고)

### 이후 (선택)
- [ ] 3D 뷰어 내장, Multi-Image to 3D, Text to 3D, 일괄 처리

> [!tip] 단계별 git 태그
> 각 단계가 끝날 때마다 `phase-1`, `phase-2` … 태그를 남기고, 블로그 글에 해당 태그 링크를 건다.

---

## 8. Meshy Docs 참고 링크 남기는 규칙

1. **코드 주석**: API를 호출하는 함수의 docstring에 `Ref: <문서 URL>`을 적는다.
2. **`docs/API_REFERENCES.md`**: 기능 · 엔드포인트 · 문서 링크 · 확인한 날짜를 표로 정리한다. → [[Meshy API 참고 문서]]
3. **블로그 글**: API를 다루는 글 끝에 "참고 문서" 섹션을 둔다.

```python
def create_image_to_3d(self, image_path: str, **options) -> str:
    """이미지로 3D 생성 작업을 만들고 task_id를 반환한다.

    Ref: https://docs.meshy.ai/api/image-to-3d  (Create an Image to 3D Task)
    """
```

---

## 9. 배포 시 주의사항

- **macOS Gatekeeper**: 서명하지 않은 앱은 경고가 뜬다. 정식 서명·공증에는 Apple Developer 계정(연 $99)이 필요하다. 초기에는 "우클릭 → 열기"로 안내한다.
- **Windows SmartScreen**: 서명하지 않은 exe는 경고가 뜬다. "추가 정보 → 실행"으로 안내한다.
- **README 고지**: "Meshy 비공식 클라이언트이며, 사용자 본인의 API 키와 크레딧을 사용함"을 명시한다.

---

## 10. 결정 로그

- 2026-11-18: 스택은 Python + PySide6 + PyInstaller로 결정
- 2026-11-18: Mac 먼저(v0.1.0), Windows는 12월(v0.2.0)
- 2026-11-18: 배포는 GitHub Release, 급한 사용자는 BUILD.md로 직접 빌드
- 2026-11-18: API 연동마다 Meshy Docs 링크를 남긴다 (코드 · docs · 블로그)
