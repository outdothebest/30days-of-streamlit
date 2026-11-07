# Streamlit 앱을 GitHub에 업로드하기

## GitHub

Git은 코드의 모든 변경 사항을 추적하는 소프트웨어입니다. 이를 버전 관리라고 합니다. GitHub는 데이터와 코드를 웹에 공개할 수 있는 Git 저장소 호스팅 서비스로, 팀이 협업하고 다른 사람이 저장소에 기여할 수 있도록 해 줍니다.

Streamlit 앱을 GitHub 저장소에 올려 두면 코드를 보관하고 공유할 수 있습니다. 다음 챌린지에서는 원하는 경우 클라우드에 배포하는 방법도 살펴봅니다. 계정 없이 로컬 실습을 계속해도 됩니다.

## GitHub 가입하기

먼저 [GitHub](https://github.com/) 계정을 만듭니다.

## GitHub 저장소 만들기

다음 단계에 따라 GitHub 저장소를 만듭니다.
- 오른쪽 위의 **"+"** 아이콘을 클릭하면 드롭다운 메뉴가 나타납니다. 여기서 **"New repository"**를 클릭합니다(*그림 1*).

- **"Create a new repository"**라는 새 웹페이지가 열립니다. **"Repository name"** 필드에 저장소 이름을 입력합니다. 예를 들어 `helloworld`라고 입력합니다(***그림 2***).

- **"Initialize this repository with:"** 항목 아래의 **"Add a README file"**을 선택합니다.

- 마지막으로 **"Create repository"**를 클릭합니다(그림 3).

새로 만든 저장소는 `https://github.com/dataprofessor/helloworld`에서 확인할 수 있습니다. 여기서 `dataprofessor`는 사용자 이름이고 `helloworld`는 저장소 이름입니다.

아래는 새로 만든 저장소의 스크린샷입니다(그림 4).

## GitHub 저장소에 파일 업로드하기

실습 폴더의 `app.py` 등 공유할 코드를 선택하세요. `.streamlit/secrets.toml`과 실제 비밀 정보는 업로드하지 마세요. 제공된 `.gitignore`는 Git으로 작업할 때 secrets 파일을 제외하지만, 웹에서 직접 올릴 때는 파일을 직접 확인해야 합니다.

파일 목록 바로 위, 초록색 **Code** 버튼 옆의 **Add file** > **Upload files**를 클릭합니다(그림 5).

새 웹페이지가 열리고 가운데 상자에 ***Drag files here to add them to your repository***와 **choose your files**가 표시됩니다. 이 상자에 파일을 끌어다 놓거나 **choose your files** 링크를 클릭하여 로컬 컴퓨터에서 파일을 선택할 수 있습니다.

**Commit changes**를 클릭하여 계속 진행합니다(그림 6).
