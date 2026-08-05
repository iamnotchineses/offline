# 오프라인 재고 정체 현황 리포트

백화점·위탁 매장에 나가 있는 오프라인 재고의 체류일과 회수 정책 적용 대상을 정리한 리포트입니다.
기준일 **2026-08-05**.

- 리포트: `index.html` (정적 HTML 한 파일, 외부 의존성은 웹폰트뿐)
- 인쇄본: `offline-inventory-report.pdf` (A4 6페이지)

## 담은 내용

| 구분 | 내용 |
|---|---|
| 원칙 1 | 오프라인 재고 비중은 50%를 넘지 않는다 |
| 원칙 2 | 45일 미판매 재고는 회수한다 |
| A | 수량 비중 vs 금액 비중 |
| B | 매장 체류 구간 분포 (45일 경계) |
| C | 매장별 정체 강도 |
| D | 45일 미판매 회수 대상 |
| E | 오프 비중 50% 초과 재고 |
| F | 브랜드별 묶인 금액 |
| G | 회수 정책 4-1 / 4-2 / 4-3 |

## GitHub Pages로 게시하기

```bash
git init
git add .
git commit -m "오프라인 재고 정체 현황 리포트"
git branch -M main
git remote add origin https://github.com/<계정>/<저장소>.git
git push -u origin main
```

푸시 후 저장소의 **Settings → Pages**에서 Source를 `Deploy from a branch`,
Branch를 `main` / `/ (root)`로 지정하면 1~2분 뒤 아래 주소로 공개됩니다.

```
https://<계정>.github.io/<저장소>/
```

`.nojekyll`은 Jekyll 빌드를 건너뛰게 하는 빈 파일입니다. 지우지 마세요.

## 갱신 방법

`index.html`을 새 버전으로 교체하고 커밋·푸시하면 됩니다.
헤더의 기준일 표기(`기준일 2026-08-05`)도 함께 바꿔 주세요.

## 공개 전 확인

이 리포트에는 매장명, 브랜드명, 재고 금액이 그대로 담겨 있습니다.
공개 저장소에 올리면 누구나 열람하고 검색엔진에도 노출됩니다.
사내 공유 목적이라면 **Private 저장소 + GitHub Pages(Enterprise)** 또는
사내 서버 배포를 권합니다.
