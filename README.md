<h1>Burpy Image Classification</h1>
<h3>Django + Google Inception V3</h3>
<p>Burpy Unity 앱에서 사용자로부터 받은 음료 이미지를 분류하는 서버.
Django로 서버를 구축하였으며, Heroku Cloud에 탑제시켰다.
서버에 Image Classification 앱을 만들었고, 이 앱에 학습된 Inception 모델을 설치하였다.
해당 앱의 url로 이미지가 동봉된 UnityWebRequest가 전달되면, 모델은 Classification을 진행하여 나온 결과물을 Burpy Wiki App (Node.js)에 전달한다.
