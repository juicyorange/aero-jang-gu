# Aero Jang-gu
IMU 센서를 부착한 전자 장구채를 통한 장구 연주

## 요약
악기를 연주하기 위해서는 악기가 필요하다. 그 중에서도 타악기들은 휴대성과 방음의 측면에서 단점이 존재한다. 두드려서 울리는 소리로 연주하기 때문에 시간 및 공간 측면에서 제약이 생기고, 그 부피 또한 크기 때문에 휴대성이 떨어진다는 것이 그 예들이다. 한국의 전통 타악기 중 하나인 장구도 위와 같은 한계가 존재한다. 이러한 한계를 극복하고자 전자 장구를 제안하고자 한다. 이에 관성 측정 장치(IMU)을 활용하여 가속도와 각속도를 활용하여 장구를 연주하는 전자 장구 채를 제안하고자 한다.

## 구성원

|구분|성명|학번|소속학과|학년|이메일|
|---|---|:-:|:-:|:-:|:-:|
|학생|김태영|2017103978|컴퓨터공학과|4|rlaxodud9809@khu.ac.kr |

## 연구배경
악기를 연주하기 위해서는 악기가 필요하다. 그 중에서도 타악기들은 휴대성과 방음의 측면에서 단점이 존재한다. 두드려서 울리는 소리로 연주하기 때문에 생기는 시간, 공간적인 한계와, 부피가 크기 때문에 생기는 휴대성이 떨어진다는 한계가 존재한다. 국외 타악기 중 하나인 드럼의 경우 허공에 드럼 스틱을 이용하여 연주하면, 카메라를 통해 모션을 인식하고 음을 출력해주는 [AeroDrums](https://aerodrums.com)가 존재한다. 드럼 스틱과 컴퓨터만 있다면 연주할 수 있기 때문에 휴대성이 뛰어나고, 컴퓨터로 음을 출력하기 때문에 시간 및 공간에 제약 없이 연주하는 것이 가능하다.

이에 본 연구에서는 한국의 전통 타악기인 장구를 전자화 하고자 한다. 관성 측정 장치(IMU)의 가속도센서(Acceleration), 각속도센서(Gyroscope)를 통해 얻은 가속도와 각속도를 활용하여 타법을 분류하고, 어느 정도의 세기로 쳤는지 파악하여 그에 맞는 음을 출력할 수 있도록 한다. 이를 통해 장구가 타악기이기에 가지는 여러 한계를 극복할 수 있는 전자 장구채를 제안하고자 한다.




## 프로젝트 소개


<p align='center'>

|프로젝트 구조|IMU+장구채|
|:-:|:-:|
| <img src ="https://user-images.githubusercontent.com/30497935/204170198-0be2510e-05bc-4af8-ac65-e2dbcccb737d.png" width="350"/> | <img src ="https://user-images.githubusercontent.com/30497935/205558309-07c504e9-6ee6-46dc-879c-7bcbe3778381.jpeg" width="350"/> |

</p>


### 모델 생성

- 모델 생성 (데이터를 추가하여 새로운 모델을 생성하고 싶은 경우)

  - 데이터 수집

    `./Arduino/GET_MOTION_SAMPLE/GET_MOTION_SAMPLE.ino` 를 실행한 뒤 진행한다.

    ```sh
    python ./python/get_sample.py <Arduino Port> <Buadrate>
    ```

  - 학습
    ```sh
    python ./python/learn.py
    ```

### 연주
  - `./Arduino/PLAY/PLAY.ino` 를 실행한 뒤 진행한다.

    ```sh
    python ./python/play.py <Arduino Port> <Buadrate>
    ```


## 데이터 분석

### 수집 데이터 형식

수집한 데이터 형식은 아래와 같다. 시계열 데이터로 하나의 타법에 대해 가속도, 각속도 정보를 수집한다.

<p align='center'>

|수집 각속도, 가속도 raw data|
|:-:|
|<img height="350" alt="raw_sample_data" src="https://user-images.githubusercontent.com/30497935/205561820-5d67b051-d08d-41c7-9671-cf43084f261b.png">|

</p>

### 전체 데이터

수집한 각속도, 가속도 값을 그래프로 그리면 아래 사진과 같다.

<p align='center'>

|따 (각속도, 가속도)|덕 (각속도, 가속도)|
|:-:|:-:|
|<img height="350" alt="dda_all_data" src="https://user-images.githubusercontent.com/30497935/204171341-f96e4aab-55cb-40a9-87eb-e259c04b817e.png">|<img height="350" alt="duck_all_data" src="https://user-images.githubusercontent.com/30497935/204171358-bf5d4607-5cc2-4c7b-8b8f-530dd2d4bc24.png">|

</p>

<p align='center'>

|따 (가속도)|덕 (가속도)|
|:-:|:-:|
|<img height="350" alt="dda_accel_data" src="https://user-images.githubusercontent.com/30497935/204171889-63c75b46-05d1-4bae-afb4-aa699ffbb9fe.png">|<img height="350" alt="duck_accel_data" src="https://user-images.githubusercontent.com/30497935/204172041-51cd209b-01a4-48d3-a022-f75cfaeb21ec.png">|

</p>

<p align='center'>

|따 (각속도)|덕 (각속도)|
|:-:|:-:|
|<img height="350" alt="dda_gyro_data" src="https://user-images.githubusercontent.com/30497935/204173395-d389e7bf-4812-4ab2-bee1-5e52e839795c.png">|<img height="350" alt="duck_gyro_data" src="https://user-images.githubusercontent.com/30497935/204173417-4a9454c1-5561-45cc-96ca-874f0d28af9b.png">|

</p>

### 타격 지점 및 세기 구분
위 데이터들을 보면 타격 지점에서 값들이 급변하는 것을 확인할 수 있다.<br>
이를 통해 타격 지점 및 타격 세기를 구분할 수 있도록 한다.

### 타법 구분
위 사진에서 보면 x축 각속도가 가장 유의미한 차이를 보이는 것을 볼 수 있다.<br>
'따' 의 경우 증가했다 감소하고, '덕' 의 경우 계속 감소하기만 한다. 따라서 이 데이터를 활용하여 학습을 진행했다.<br>
분석에 활용한 데이터는 아래와 같다.

<p align='center'>

|따 (x축 각속도)|덕 (x축 각속도)|
|:-:|:-:|
|<img height="350" alt="dda_x_gyro_data" src="https://user-images.githubusercontent.com/30497935/204173584-23873681-7d8a-49fe-8093-97958ee71491.png">|<img height="350" alt="duck_x_gyro_data" src="https://user-images.githubusercontent.com/30497935/204173592-68e1bdca-9b79-4985-88bb-c7cfb4ab10c2.png">|

</p>

나머지 데이터는 아래와 같다. 데이터들을 확인하면 타격 지점에서 값들이 급변하는 것을 확인할 수 있다.<br>
이를 통해 충격 지점 및 타격 세기를 확인한다.



## 결과

SVC 모델을 통해 학습한 결과는 아래와 같다.
|데이터 1개|데이터 전체|
|:-:|:-:|
|<img width="400" alt="svc_line_1" src="https://user-images.githubusercontent.com/30497935/204174055-02d0154a-b4ea-4dd1-ae6f-f381a53f0061.png">|<img width="400" alt="svc_line_50" src="https://user-images.githubusercontent.com/30497935/204173982-c96c4864-e9dd-4dbd-8191-52184e28b4fa.png">|

연주하는 영상은 아래와 같다.
|덕|따|
|:-:|:-:|
|<img alt="duck" src ="https://user-images.githubusercontent.com/30497935/205558504-7a784bdd-89b9-4949-9a6c-315ed9447b2a.mp4" width="400px">|<img alt="dda" src ="https://user-images.githubusercontent.com/30497935/205559370-0daafff9-2324-4d19-92c9-e578b102ad11.mp4" width="400px">|


## 기대효과
전자 장구채를 이용하면 시공간 및 휴대성 측면에서의 한계를 극복할 수 있다. 이를 통해 언제 어디서든 편리하게 장구를 연주할 수 있을 것이다.