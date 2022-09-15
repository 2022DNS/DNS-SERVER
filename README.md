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

```bash
$ git clone https://github.com/2022DNS/DNS-SERVER
$ cd DNS-SERVER
$ pip install -r requirements.txt
$ python manage.py runserver
```

## <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Amazon CloudWatch</title><path d="M18.454 14.905c0-1.676-1.372-3.039-3.059-3.039-1.686 0-3.058 1.363-3.058 3.039 0 1.675 1.372 3.038 3.058 3.038 1.687 0 3.059-1.363 3.059-3.038Zm.862 0c0 2.147-1.759 3.894-3.92 3.894-2.162 0-3.92-1.747-3.92-3.894 0-2.148 1.758-3.895 3.92-3.895 2.161 0 3.92 1.747 3.92 3.895Zm3.617 5.87-3.004-2.688c-.242.34-.523.649-.834.926l2.999 2.687c.256.23.654.208.885-.046a.623.623 0 0 0-.046-.88Zm-7.538-1.206c2.59 0 4.696-2.092 4.696-4.664 0-2.573-2.106-4.665-4.696-4.665-2.589 0-4.696 2.092-4.696 4.665 0 2.572 2.107 4.664 4.696 4.664Zm8.224 2.658c-.293.323-.7.487-1.107.487a1.49 1.49 0 0 1-.995-.378L18.399 19.542a5.543 5.543 0 0 1-3.004.883c-3.064 0-5.557-2.476-5.557-5.52 0-3.044 2.493-5.521 5.557-5.521 3.065 0 5.558 2.477 5.558 5.52 0 .874-.21 1.697-.576 2.432l3.133 2.803c.608.546.657 1.482.11 2.088ZM3.977 7.454c0 .222.014.444.04.659a.426.426 0 0 1-.352.473C2.605 8.858.862 9.681.862 12.148c0 1.863 1.034 2.892 1.902 3.427.297.185.647.284 1.017.288l5.195.005v.856l-5.2-.005a2.815 2.815 0 0 1-1.469-.418C1.447 15.77 0 14.524 0 12.148c0-2.864 1.971-3.923 3.129-4.297a6.093 6.093 0 0 1-.013-.397c0-2.34 1.598-4.767 3.716-5.645 2.478-1.031 5.104-.52 7.022 1.367a7.048 7.048 0 0 1 1.459 2.116 2.79 2.79 0 0 1 1.78-.644c1.287 0 2.735.97 2.993 3.092 1.205.276 3.751 1.24 3.751 4.441 0 1.278-.403 2.333-1.199 3.137l-.614-.6c.632-.638.952-1.491.952-2.537 0-2.8-2.36-3.495-3.374-3.664a.43.43 0 0 1-.353-.496c-.141-1.738-1.18-2.517-2.156-2.517-.616 0-1.193.298-1.584.818a.431.431 0 0 1-.75-.111c-.353-.971-.861-1.788-1.511-2.426-1.663-1.636-3.936-2.079-6.084-1.186-1.787.74-3.187 2.873-3.187 4.855Z"/></svg> API 가이드(API Guide)


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
