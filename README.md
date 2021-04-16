<h1>Burpy Image Classification (2018)</h1>
<p>해당 페이지에서 Burpy 프로젝트의 Image Classification 서버를 소개합니다.</p>

<h2>Tech Stack</h2>
<ul>
  <li>Programming Language</li>
  <ul>
    <li><img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></li>
  </ul>
  <li>Framework</li>
  <ul>
    <li><img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/></li>
    <li><img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=Tensorflow&logoColor=white"/></li></li>
  </ul>
  <li>Public Cloud</li>
  <ul>
    <li><img src="https://img.shields.io/badge/Heroku Free Account-430098?style=flat-square&logo=Heroku&logoColor=white"/></li></li>
  </ul>
</ul>

<h2>Summary</h2>
<p>Unity의 Burpy App으로부터 전달받은 이미지 파일 (스캔된 음료 이미지)을 학습된 모델로 분류시키는 ML 서버입니다.  이를테면, 코카콜라에 대한 이미지를 제시하면 분류시 가장 높은 매칭을 보이는 카테고리가 제시됩니다 (e.g. 1순위 코카콜라 2순위 코카콜라 제로 3순위 닥터페퍼).</p>

<h2>Detail</h2>
<p>Django Web Framework로 서버를 구축하였으며, 이 서버에 Image Classification 앱을 구성했습니다.
해당 앱에 Inception v3를 튜닝하여 학습시킨 모델을 인스톨하였습니다.</p>

![Burpy Web Request Model](https://user-images.githubusercontent.com/30020288/115008260-def17e80-9ee5-11eb-87b3-c0491de9417f.png)

<ol>
  <li>Unity로부터 이미지 사진이 포함된 Request를 Image Classification의 URL로부터 수용합니다.</li>
  <li>Request를 파싱하여, 이미지 파일의 배열을 Classification의 Input으로 사용합니다.</li>
  <li>Classification의 5순위 결과를 반환하여, Node.js 서버 (음료 위키 서버)에 전달합니다.</li>
</ol>

<h2>Behind Story</h2>
<p>아무래도 Heroku 서버 규모가 Free Account이다보니, 서버 역할의 제한이 많았습니다. 기존 계획에는 모델 업데이트도 추가할 예정이었으나, Request만 받으면 서버가 버티질 못하고 뻗었습니다. 당시 프로젝트 마감 기간일 뿐더러, ACM VRST2018에 투고할 Short Paper를 준비하고 있어 클라우드 이전을 고려하지 못한게 아쉬움으로 남았습니다. 프론트-백엔드 프로그래밍이 미숙하기도 하여, 모델 업데이트는 수기로 업데이트하는 방향으로 프로젝트를 진행했습니다.</p>
<p>모델의 Training Data는 Google Drive에서 관리하도록 설정하였습니다.</p>

<h2>Check This</h2>
<a href="https://github.com/boosilguy/Burpy">Burpy Unity App</a>
