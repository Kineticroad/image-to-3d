# Image to 3D

이미지 한 장을 올리면 [Meshy AI](https://www.meshy.ai)의 Image to 3D API로 3D 모델을 만들어 주는 데스크톱 앱입니다.

<a href="https://buymeacoffee.com/igna84" target="_blank"><img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy me a coffee"></a>

> [!IMPORTANT]
> **비공식 클라이언트 애플리케이션입니다.**
>
> - 이 프로젝트는 Meshy AI와 관계없는 **개인 프로젝트**입니다. Meshy AI가 만들거나 승인, 후원, 검토한 앱이 아닙니다.
> - **Meshy AI의 광고가 아닙니다.** Meshy AI로부터 어떤 대가나 지원도 받지 않았습니다.
> - 내가 **직접 비용을 내고 Meshy AI를 구독해서** 개발하고 있습니다.
> - 개발자는 [Buy Me a Coffee](#후원)로 **개인 후원**을 받고 있습니다. 이 후원은 Meshy AI와 관계없습니다.
> - 이 앱을 쓰려면 사용자 **본인의 Meshy API 키**가 필요하고, 모델을 만들 때 **본인 계정의 크레딧**이 차감됩니다.
> - 업로드한 이미지는 3D 변환을 위해 Meshy AI 서버로 전송됩니다. 아래 [업로드 이미지 주의사항](#업로드-이미지-주의사항)을 꼭 읽어 주세요.
> - "Meshy"는 해당 회사의 상표이며, 이 문서와 앱에서는 연동하는 서비스를 설명하는 데에만 사용합니다.
> - 사용자는 [Meshy 이용약관](https://www.meshy.ai/terms-of-use)과 [허용 가능한 사용 정책](https://www.meshy.ai/acceptable-use-policy)을 지켜야 합니다.

## 업로드 이미지 주의사항

> [!CAUTION]
> **업로드한 이미지는 이 앱이 아니라 Meshy AI 서버로 전송되어 처리·보관됩니다.**
>
> - **사람 얼굴, 이름, 주소, 연락처, 신분증, 차량 번호판 등 개인을 알아볼 수 있는 정보가 담긴 이미지는 올리지 마세요.**
>   Meshy 이용약관(§2.2)은 본인이나 제3자의 개인 식별 정보를 입력에 넣는 것을 금지합니다.
> - **다른 사람이 저작권을 가진 이미지는 올리지 마세요.** (Meshy 허용 가능한 사용 정책 §3)
> - Meshy는 Enterprise가 아닌 고객이 올린 이미지와 생성 결과물을 **AI 학습과 서비스 개선에 사용할 수 있습니다** (이용약관 §2.9).
>   원하지 않으면 support@meshy.ai 로 직접 거부(opt-out)를 요청해야 합니다.
> - 업로드한 이미지와 생성 결과물이 어떻게 저장되고 사용되는지는 [Meshy 개인정보처리방침](https://www.meshy.ai/privacy-policy)을 따릅니다.
>
> **면책:** 이 앱의 개발자는 업로드한 이미지가 Meshy AI 서버로 전송된 뒤의 저장, 처리, 학습 사용, 그리고 그로 인한 **개인정보 유출이나 권리 침해에 대해 어떠한 책임도 지지 않습니다.**
> 어떤 이미지를 올릴지는 전적으로 사용자 본인의 판단과 책임입니다.

## 작업 분담

### 기획: Kineticroad(igna84, a.k.a. 야훔)

- 요구사항 정의, 기술 스택 선정, 로드맵, 배포 전략 등 프로젝트 기획을 직접 진행했습니다.
- 기획 문서는 [`.claude/`](.claude/) 폴더에 있습니다.

### 디자인 · UI: AI (Claude Code)

> **이 부분은 AI가 작업을 진행했습니다.**
>
> 위 기획 문서를 토대로 AI(Claude Code)가 작업했습니다.

- **UI 디자인**: Figma MCP를 이용해 Figma에서 화면을 디자인했습니다.
- **PySide6 Designer UI**: 디자인을 바탕으로 Qt Designer용 `.ui` 파일과 변환된 `.py` 파일을 만들었습니다.
  - [`src/ui/main_window.ui`](src/ui/main_window.ui), [`src/ui/settings_dialog.ui`](src/ui/settings_dialog.ui), [`src/ui/job_item.ui`](src/ui/job_item.ui)
  - [`src/ui/styles/dark.qss`](src/ui/styles/dark.qss), [`src/ui/icons/`](src/ui/icons/)
- **창 실행 코드**: 변환된 UI를 창으로 띄우는 코드를 작성했습니다.
  - [`src/ui/windows.py`](src/ui/windows.py), [`src/main.py`](src/main.py)

## 실행

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirement.txt
python src/main.py
```

## UI 수정 방법

화면의 원본은 `.ui` 파일입니다. Qt Designer에서 `.ui`를 고친 뒤 아래처럼 다시 변환하고, `.ui`와 `.py`를 함께 커밋합니다.

```bash
pyside6-uic src/ui/main_window.ui -o src/ui/main_window.py
```

> [!NOTE]
> PySide6 6.12.0의 `pyside6-uic`는 스핀박스의 `showGroupSeparator` 속성을 존재하지 않는 `setShowGroupSeparator()`로 변환합니다. `main_window.py`를 다시 변환한 뒤에는 이 줄을 `setGroupSeparatorShown()`으로 고쳐야 실행됩니다.
>
> ```bash
> sed -i '' 's/setShowGroupSeparator(/setGroupSeparatorShown(/' src/ui/main_window.py   # macOS
> ```

## 후원

이 프로젝트가 도움이 됐다면 커피 한 잔으로 응원해 주세요.

<a href="https://buymeacoffee.com/igna84" target="_blank"><img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy me a coffee"></a>

- 후원은 **개발자 개인에 대한 자발적인 후원**입니다. Meshy AI와는 관계없으며, Meshy AI에 전달되지 않습니다.
- 후원해도 **기능, 크레딧, 기술 지원이 추가되지 않습니다.** 앱은 후원 여부와 관계없이 누구나 무료로 쓸 수 있습니다.
- 후원금은 Meshy 서비스나 크레딧의 대가가 아닙니다. 모델 생성에 드는 크레딧은 사용자 본인의 Meshy 계정에서 Meshy에 직접 결제됩니다.

## 라이선스

이 프로젝트의 소스 코드는 [MIT 라이선스](LICENSE)로 배포됩니다.

이 소프트웨어는 **있는 그대로(AS IS)** 제공되며, 사용으로 생긴 손해(크레딧 차감, 데이터 손실, 개인정보 유출 등)에 대해 개발자는 책임지지 않습니다.

### 사용한 오픈소스

| 라이브러리 | 라이선스 | 용도 |
|---|---|---|
| [PySide6 (Qt for Python)](https://doc.qt.io/qtforpython-6/) | **LGPL-3.0** | GUI |
| [httpx](https://github.com/encode/httpx) | BSD-3-Clause | Meshy API 통신 |
| [httpx-sse](https://github.com/florimondmanca/httpx-sse) | MIT | 진행률 스트림(SSE) |
| [keyring](https://github.com/jaraco/keyring) | MIT | API 키를 OS 보안 저장소에 보관 |

> [!NOTE]
> **PySide6 / Qt는 LGPL-3.0 라이선스입니다.**
>
> - 이 프로젝트는 PySide6를 수정하지 않고 라이브러리로 **동적 링크해서 사용**합니다. 이 프로젝트의 MIT 라이선스는 PySide6와 Qt에는 적용되지 않습니다.
> - 배포하는 실행 파일(`.app` / `.exe`)에는 PySide6와 Qt 라이브러리가 함께 들어 있으며, 해당 라이브러리는 LGPL-3.0을 따릅니다.
> - 사용자는 LGPL-3.0에 따라 앱에 포함된 PySide6/Qt 라이브러리를 다른 버전으로 교체할 권리가 있습니다.
> - PySide6 / Qt 소스 코드: https://code.qt.io/cgit/pyside/pyside-setup.git/ · 라이선스 전문: https://www.gnu.org/licenses/lgpl-3.0.html
