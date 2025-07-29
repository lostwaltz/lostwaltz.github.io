---
title: HUGO STACK 테마 적용하기
description: STACK 테마 GITPAGE를 배포하는 법을 정리합니다.
date: 2025-07-08 00:00:00+0000
image:
categories:
    - 문서
tags:
    - HUGO
weight: 1      # You can add weight to some posts to override the default sorting (date descending)
---

---
# HUGO STACK 테마로 블로그 개설하기

이번 포스트는 **STACK** 테마의 블로그를, **GITPAGE**를 통해 만든 과정을 정리해보겠습니다.

1. **HUGO** 다운로드.
2. **GO** 다운로드.

GIT의 경우, 다운로드 된 가정하에 진행합니다.

## HUGO 다운로드

1. [HUGO ](https://github.com/gohugoio/hugo/releases/tag/v0.148.2) window/extended 버젼을 다운로드 받습니다.
2. 압축을 해제하고, HUGO.exe 파일이 있는 폴더를 환경변수 PATH에 등록합니다.

## 테마 다운로드

1. [STACK ](https://stack.jimmycai.com/)에서, 템플릿을 통해 리포지토리를 생성합니다.
2. 레포지토리 생성시 이름을 0000/github.io 로 맞춰줍니다.

## GO 다운로드

**CODESPACE**를 생성하면 hugo serve 명령어를 통해 로컬 호스팅을 진행할 수 있지만    
코드 스페이스의 로컬이기 때문에 연결이 되지 않습니다.

때문에 **GO**를 다운로드 받고, 로컬 서버를 열 수 있도록 해봅시다.

1. [GO ](https://go.dev/dl/)에서, 알맞는 OS에의 파일을 받습니다.
2. go version 명령어를 통해, 설치를 확인합니다.
3. 리포지토리의 로컬 폴더에서, git serve 명령어를 실행합니다.
4. 테마가 적용된 상태의 로컬 블로그를 확인합니다.

## 실제 페이지 배포

**STACK**에서 굉장히 편한 방법을 제공 해준 덕분에, 벌써 모든 준비가 끝났고 배포만 진행하면 됩니다.

1. Setting/Page에서 gh-pages로 변경 후 **SAVE** 합니다.
2. ReedMe 파일을 삭제 합니다.
2. 커밋, 푸쉬를 진행 하면, gitpages를 통해 실제 페이지를 확인 할 수 있습니다! 

### 끝내며

적용 방법들 포스트를 많이 찾아 봤었는데, 원래 방법은 submodule 등, theme를 받아와 배포하고, 설정 할게 많았으나
감사하게도 쉽게 시작할 수 있도록 STARTER 패키지를 내주어 쉽게 적용 할 수 있었습니다.

컴퓨터를 밀고 나면, 참고하려고 페이지를 방문하는 제가 있겠네요.

---

