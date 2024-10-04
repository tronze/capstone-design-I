# Capstone Design I
서강대학교 Capstone Design I 수업을 위한 팀 WingIt의 프로젝트입니다.

## Branch
Branch는 기본적으로 2개로 운영할 예정입니다.
- master (배포용 브랜치입니다)
- dev (개발용 브랜치입니다)
  
배포용 브랜치(master)는 최종 코드만 올라가 있는 브랜치입니다. 담당자가 PR을 통해 작업 완료된 코드를 합치는 경우를 제외하고는 건드리지 않습니다.

개발용 브랜치(dev)는 어느 정도 작업이 완료된 코드를 합치는 경우에 활용합니다. 대부분 배포용 브랜치(master)에 코드를 합치기 전에 완료된 작업이 이전 작업과 충돌이 없이 잘 돌아가는지 확인하는 용도입니다.
또는 작업 중이던 코드를 지속적으로 합쳐서 개발되는 과정(기획 의도대로 개발이 진행되는지, 또는 기획에서 생각한 형태나 느낌이 맞는지 등을 보며 방향을 바꿀 필요가 있는지 체크하기 위해)을 지켜보기 위해 활용하기도 합니다.

그 외로 본인 작업은 항상 따로 브랜치를 생성해서 작업을 진행하는 것을 원칙으로 합니다. 작업이 완료되거나 개발 서버 등에서 확인이 필요할 때는 dev에 PR을 요청는 형식으로 진행하겠습니다.

Commit 메세지 형태는 따로 정하지 않겠습니다. 다만 Commit Message에 어떤 작업을 진행했는지 (What) 그리고 왜 진행했는지 (Why) 등의 내용은 꼭 포함하는걸로 하겠습니다.
ex) Issue #12 해결을 위해 회원가입에 추가적으로 필요한 필드 추가.

다음 글을 읽어보시면 좋을 것 같습니다.
- [브랜치 운용 방식과 Naming Convention](https://velog.io/@kim-jaemin420/Git-branch-naming)
- [Pull Request Convention](https://puleugo.tistory.com/165)
- [Commit Message Convention](https://velog.io/@chojs28/Git-%EC%BB%A4%EB%B0%8B-%EB%A9%94%EC%8B%9C%EC%A7%80-%EA%B7%9C%EC%B9%99)
