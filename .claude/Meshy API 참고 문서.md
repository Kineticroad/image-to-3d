---
title: Meshy API 참고 문서
date: 2026-11-18
tags:
  - meshy
  - api
  - 참고자료
---

# Meshy API 참고 문서

상위 노트: [[Meshy Desktop 개발 계획]]

> [!info] 기본 정보
> - Base URL: `https://api.meshy.ai/openapi/`
> - 인증: `Authorization: Bearer <API_KEY>` (키 형식 `msy_...`)
> - API 키 발급: https://www.meshy.ai/developers/keys
> - 문서 홈: https://docs.meshy.ai
> - 변경 이력: https://docs.meshy.ai/api/changelog
> - 서비스 상태: https://status.meshy.ai

## 앱 기능 ↔ 문서 매핑

| 앱 기능 | 엔드포인트 | 참고 문서 | 확인일 |
|---|---|---|---|
| 처음 시작하기 | - | https://docs.meshy.ai/api/quick-start | 2026-11-18 |
| API 키 인증 | `Authorization: Bearer` | https://docs.meshy.ai/api/authentication | 2026-11-18 |
| 3D 생성 요청 | `POST /openapi/v1/image-to-3d` | https://docs.meshy.ai/api/image-to-3d | 2026-11-18 |
| 진행률 확인 | `GET /openapi/v1/image-to-3d/:id`, `/stream` | https://docs.meshy.ai/api/image-to-3d · https://docs.meshy.ai/api/task-lifecycle | 2026-11-18 |
| 작업 목록 / 삭제 | `GET`, `DELETE /openapi/v1/image-to-3d` | https://docs.meshy.ai/api/image-to-3d | 2026-11-18 |
| 크레딧 잔액 | `GET /openapi/v1/balance` | https://docs.meshy.ai/api/balance | 2026-11-18 |
| 에러 처리 (401·429 등) | - | https://docs.meshy.ai/api/errors | 2026-11-18 |
| 재시도 / 속도 제한 | - | https://docs.meshy.ai/api/rate-limits | 2026-11-18 |
| 결과 자동 다운로드 | - | https://docs.meshy.ai/api/asset-retention | 2026-11-18 |
| 비용 안내 | - | https://docs.meshy.ai/api/pricing | 2026-11-18 |
| 폐기 예정 파라미터 | - | https://docs.meshy.ai/api/deprecations | 2026-11-18 |
| (확장) 여러 장 → 3D | `POST /openapi/v1/multi-image-to-3d` | https://docs.meshy.ai/api/multi-image-to-3d | - |
| (확장) 텍스트 → 3D | - | https://docs.meshy.ai/api/text-to-3d | - |
| (확장) 웹훅 | - | https://docs.meshy.ai/api/webhooks | - |

## Image to 3D 핵심 메모 (2026-11-18 기준)

- **입력**: `image_url`에 공개 URL 또는 base64 data URI를 넣는다. JPG/JPEG/PNG/WebP, 최대 20MB, 한 변 32px 이상.
- **주요 옵션**
  - `ai_model`: `latest`(기본), `meshy-7.1`, `meshy-6`, `meshy-6-lite` (`meshy-7`은 폐기 예정)
  - `should_texture`: 기본 `true`
  - `enable_pbr`: 기본 `false` (metallic, roughness, normal 맵 추가)
  - `target_formats`: `glb`, `obj`, `fbx`, `stl`, `usdz`, `3mf` 중 선택
  - `pose_mode`: `a-pose`, `t-pose` (캐릭터용)
- **상태**: `PENDING` / `IN_PROGRESS` / `SUCCEEDED` / `FAILED` / `CANCELED`, `progress`는 0~100
- **출력**: `model_urls`(glb, fbx, obj, usdz, stl, mtl), `thumbnail_url`, `texture_urls`
- **비용**: 텍스처가 있으면 30크레딧. 실패한 작업은 환불, PENDING 상태에서 삭제해도 환불된다.
- **보관**: Enterprise가 아니면 최대 3일 → 앱에서 자동 다운로드
- **Rate limit**: Pro는 초당 20요청, 동시 작업 10개. 초과하면 `429`

> [!tip] AI 에이전트용 문서
> - 전체 목차: https://docs.meshy.ai/llms.txt
> - 전체 내용 한 파일: https://docs.meshy.ai/llms-full.txt
> - OpenAPI 스펙: https://docs.meshy.ai/openapi.json
