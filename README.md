<h1 align="center"><strong>D.N.S</strong><br>우리의 안전을 지키는 졸음 탐지 오픈소스.</h1>
<p align="center">
 졸음을 탐지할 수 있는 오픈소스를 사용하여 졸음 운전을 방지하세요.
</p>
<p align="center">
  <img src="https://img.shields.io/github/repo-size/2022DNS/DNS-SERVER?style=for-the-badge"/>
  <a href = "https://github.com/2022DNS/DNS-SERVER"><img src="https://img.shields.io/badge/REPO-DNS_SERVER-informatoinal?style=for-the-badge"/></a>
  <a href = "https://github.com/2022DNS/DNS-ANDROID"><img src="https://img.shields.io/badge/REPO-DNS_ANDROID-informatoinal?style=for-the-badge"/></a>
  <br>
  
</p>
<br>
<br>

## 프로젝트 설명
<p><b>D.N.S</b>졸음운전을 인식해주는 기능을 OpenAPI로 만든 오픈소스입니다. 모바일 네비게이션 서비스 업체들에서 졸음운전 방지 기능을 쉽게 적용할 수 있도록 도와주며 이를 통해 졸음운전으로 인한 사고를 줄이고자 하는 목표를 가지고 있습니다. 저희가 만든 OpenAPI 서버와 모바일, OpenAPI간 연동을 위해 제공하는 샘플 코드, API 문서를 참고하여 쉽게 사용할 수 있습니다. 또한, 공개 프로젝트이기 때문에 추가되었으면 하는 기능이나 개선사항들을 요청(PR)할 수 있고 코드를 참고해서 네비게이션 서비스 업체들이 필요로 하는 기능에 맞게끔 직접 수정할 수도 있습니다.</p>
<br>

## 🔧 기술 스택 (Technique Used)
### Server(back-end)
 - Django
 - djangorestframework
 - mysql
 - opencv-python

## ⛏ 설치 안내 (Installation Process)
requirements.txt와 Dockerfile을 이용하여 모듈을 설치했다고 가정한다.

```bash
$ git clone https://github.com/2022DNS/DNS-SERVER
$ cd DNS-SERVER
$ python manage.py runserver
```

## 팀 정보 (Team Information)
<table width="788">
<thead>
<tr>
<th width="100" align="center">사진</th>
<th width="100" align="center">성명</th>
<th width="200" align="left">담당</th>
<th width="150" align="center">깃허브</th>
<th width="225" align="center">이메일</th>
</tr> 
</thead>
<tbody>
    <tr>
        <td width="100" align="center"><img src="/images/youngjin.png" width="60" height="60"></td>
        <td width="100" align="center">손영진</td>
        <td width="150">D.N.S팀장<br>D.N.S-Mobile 개발<br>졸음 인식 개발</td>
        <td width="100" align="center">
          <a href="https://github.com/ILoveGameCoding">
            <img src="http://img.shields.io/badge/ILoveGameCoding-655ced?style=social&logo=github"/>
          </a>
        </td>
        <td width="175" align="center">
          <a href="mailto:sonkim1001@naver.com"><img src="https://img.shields.io/static/v1?label=&message=sonkim1001@naver.com&color=blue&style=flat-square&logo=gmail"></a>
        </td>
    </tr>
    <tr>
        <td width="100" align="center"><img src="/images/junan.PNG" width="60" eight="60"></td>
        <td width="100" align="center">최준환</td>
        <td width="150">D.N.S Server 개발<br>API 설계<br>DRF 개발 등</td>
        <td width="100" align="center">
          <a href="https://github.com/junanhouse">
            <img src="http://img.shields.io/badge/junanhouse-655ced?style=social&logo=github"/>
          </a>
        </td>
        <td width="175" align="center">
          <a href="mailto:home99032@naver.com"><img src="https://img.shields.io/static/v1?label=&message=home99032@naver.com&color=orange&style=flat-square&logo=gmail"></a>
        </td>
    </tr>
    <tr>
        <td width="100" align="center"><img src="/images/sungjoon.png" width="60" height="60"></td>
        <td width="100" align="center">배성준</td>
        <td width="150">D.N.S Server 개발<br>문서 작업 등</td>
        <td width="100" align="center">
          <a href="https://github.com/westofsky">
            <img src="http://img.shields.io/badge/westofsky-655ced?style=social&logo=github"/>
          </a>
        </td>
        <td width="175" align="center">
          <a href="mailto:westofsky159@gamil.com"><img src="https://img.shields.io/static/v1?label=&message=westofsky159@gamil.com&color=critical&style=flat-square&logo=gmail"></a>
        </td>
    </tr>
</tbody>
</table>
