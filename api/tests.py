from rest_framework.test import APIClient, APITestCase
from django.test import TestCase, Client
import json


"""
테스트 케이스 명세서

1. 케이스 설정 방법
    1) success test case
        - 성공 응답 코드 
    2) error test case 
        - 에러 응답 코드

2. 케이스 종류
    1) 필수 요소 1개 (구분 코드 GUBN)
        - 구분 코드(GUBN)의 종류 25가지 : Success Test Case 25개 
        
    2) 필수 요소 1개 + 옵션 요소 2 ~ 3개 (ex. MEA_YMD, MEA_YMD2)
        - 필수 요소 (GUBN)을 default 케이스로 둔다.
        - start_index & end_index
        - Success Test Case 25개 : index 범위를 정상적으로 설정.
        - Error Test Case 50개 : (1) start_index > end_index , (2) MEA_YMD or MEA_YMD2 is None
        
3. Parameter
    - IDN : String
    - GUBN : Int
    - GUBN_NAM : String
    - MEA_YMD : YYYYMMDDHH24
    - MEA_WAL : Float
    - SIG_STA : String
"""

# Create your tests here.


class SewerLineTest(APITestCase):
    client = APIClient
    headers = {}

    def setUp(self):
        sewer1 = {
            # 'id': 1,
            # 'idn': '01-0004',
            'gubn': 1,
            'gubn_nam': '종로',
            # 'mea_ymd': '2022-06-28T00:00:58Z',
            # 'mea_wal': '0.12',
            # 'sig_sta': '통신양호'
        }
        self.sewer = sewer1

        sewer2 = {
            'gubn': 2,
            'gubn_nam': '중',
        }
        self.sewer2 = sewer2

        sewer3 = {
            'gubn': 3,
            'gubn_nam': '용산',
        }
        self.sewer3 = sewer3

        sewer4 = {
            'gubn': 4,
            'gubn_nam': '성동',
        }
        self.sewer4 = sewer4

        sewer5 = {
            'gubn': 5,
            'gubn_nam': '광진',
        }
        self.sewer5 = sewer5

        sewer6 = {
            'gubn': 6,
            'gubn_nam': '동대문',
        }
        self.sewer6 = sewer6

        sewer7 = {
            'gubn': 7,
            'gubn_nam': '중랑',
        }
        self.sewer7 = sewer7

        sewer8 = {
            'gubn': 8,
            'gubn_nam': '성북',
        }
        self.sewer8 = sewer8

        sewer9 = {
            'gubn': 9,
            'gubn_nam': '강북',
        }
        self.sewer9 = sewer9

        sewer10 = {
            'gubn': 10,
            'gubn_nam': '도봉',
        }
        self.sewer10 = sewer10

        sewer11 = {
            'gubn': 11,
            'gubn_nam': '노원',
        }
        self.sewer11 = sewer11

        sewer12 = {
            'gubn': 12,
            'gubn_nam': '은평',
        }
        self.sewer12 = sewer12

        sewer13 = {
            'gubn': 13,
            'gubn_nam': '서대문',
        }
        self.sewer13 = sewer13

        sewer14 = {
            'gubn': 14,
            'gubn_nam': '마포',
        }
        self.sewer14 = sewer14

        sewer15 = {
            'gubn': 15,
            'gubn_nam': '양천',
        }
        self.sewer15 = sewer15

        sewer16 = {
            'gubn': 16,
            'gubn_nam': '강서',
        }
        self.sewer16 = sewer16

        sewer17 = {
            'gubn': 17,
            'gubn_nam': '구로',
        }
        self.sewer17 = sewer17

        sewer18 = {
            'gubn': 18,
            'gubn_nam': '금천',
        }
        self.sewer18 = sewer18

        sewer19 = {
            'gubn': 19,
            'gubn_nam': '영등포',
        }
        self.sewer19 = sewer19

        sewer20 = {
            'gubn': 20,
            'gubn_nam': '동작',
        }
        self.sewer20 = sewer20

        sewer21 = {
            'gubn': 21,
            'gubn_nam': '관악',
        }
        self.sewer21 = sewer21

        sewer22 = {
            'gubn': 22,
            'gubn_nam': '서초',
        }
        self.sewer22 = sewer22

        sewer23 = {
            'gubn': 23,
            'gubn_nam': '강남',
        }
        self.sewer23 = sewer23

        sewer24 = {
            'gubn': 24,
            'gubn_nam': '송파',
        }
        self.sewer24 = sewer24

        sewer25 = {
            'gubn': 25,
            'gubn_nam': '강동',
        }
        self.sewer25 = sewer25



    """
    필수 요소 : GUBN
    Success Test Case : 25개
    method : GET
    param : gubn
    """
    def test_necessary_success01(self):
        response = self.client.get('/api/sewer/?search=1', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer1['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success02(self):
        response = self.client.get('/api/sewer/?search=2', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer2['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success03(self):
        response = self.client.get('/api/sewer/?search=3', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer3['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success04(self):
        response = self.client.get('/api/sewer/?search=4', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer4['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success05(self):
        response = self.client.get('/api/sewer/?search=5', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer5['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success06(self):
        response = self.client.get('/api/sewer/?search=6', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer6['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success07(self):
        response = self.client.get('/api/sewer/?search=7', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer7['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success08(self):
        response = self.client.get('/api/sewer/?search=8', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer8['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success09(self):
        response = self.client.get('/api/sewer/?search=9', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer9['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success010(self):
        response = self.client.get('/api/sewer/?search=10', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer10['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success011(self):
        response = self.client.get('/api/sewer/?search=11', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer11['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success012(self):
        response = self.client.get('/api/sewer/?search=12', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer12['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success013(self):
        response = self.client.get('/api/sewer/?search=13', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer13['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success014(self):
        response = self.client.get('/api/sewer/?search=14', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer14['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success015(self):
        response = self.client.get('/api/sewer/?search=15', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer15['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success016(self):
        response = self.client.get('/api/sewer/?search=16', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer16['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success017(self):
        response = self.client.get('/api/sewer/?search=17', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer17['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success018(self):
        response = self.client.get('/api/sewer/?search=18', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer18['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success019(self):
        response = self.client.get('/api/sewer/?search=19', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer19['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success020(self):
        response = self.client.get('/api/sewer/?search=20', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer20['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success021(self):
        response = self.client.get('/api/sewer/?search=21', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer21['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success022(self):
        response = self.client.get('/api/sewer/?search=22', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer22['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success023(self):
        response = self.client.get('/api/sewer/?search=23', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer23['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success024(self):
        response = self.client.get('/api/sewer/?search=24', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer24['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_success025(self):
        response = self.client.get('/api/sewer/?search=25', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer25['gubn'])
        self.assertEqual(response.status_code, 200)

    """
    필수 요소 : GUBN
    Fail Test Case : 25개
    method : GET
    param : gubn
    """
    def test_necessary_fail01(self):
        response = self.client.get('/api/sewer/?search=1', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer2['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail02(self):
        response = self.client.get('/api/sewer/?search=2', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer3['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail03(self):
        response = self.client.get('/api/sewer/?search=3', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer4['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail04(self):
        response = self.client.get('/api/sewer/?search=4', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer5['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail05(self):
        response = self.client.get('/api/sewer/?search=5', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer6['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail06(self):
        response = self.client.get('/api/sewer/?search=6', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer7['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail07(self):
        response = self.client.get('/api/sewer/?search=7', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer8['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail08(self):
        response = self.client.get('/api/sewer/?search=8', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer9['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail09(self):
        response = self.client.get('/api/sewer/?search=9', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer10['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail010(self):
        response = self.client.get('/api/sewer/?search=10', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer11['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail011(self):
        response = self.client.get('/api/sewer/?search=11', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer12['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail012(self):
        response = self.client.get('/api/sewer/?search=12', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer13['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail013(self):
        response = self.client.get('/api/sewer/?search=13', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer14['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail014(self):
        response = self.client.get('/api/sewer/?search=14', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer15['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail015(self):
        response = self.client.get('/api/sewer/?search=15', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer16['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail016(self):
        response = self.client.get('/api/sewer/?search=16', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer17['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail017(self):
        response = self.client.get('/api/sewer/?search=17', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer18['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail018(self):
        response = self.client.get('/api/sewer/?search=18', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer19['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail019(self):
        response = self.client.get('/api/sewer/?search=19', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer20['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail020(self):
        response = self.client.get('/api/sewer/?search=20', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer21['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail021(self):
        response = self.client.get('/api/sewer/?search=21', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer22['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail022(self):
        response = self.client.get('/api/sewer/?search=22', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer23['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail023(self):
        response = self.client.get('/api/sewer/?search=23', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer24['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail024(self):
        response = self.client.get('/api/sewer/?search=24', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer25['gubn'])
        self.assertEqual(response.status_code, 200)
    def test_necessary_fail025(self):
        response = self.client.get('/api/sewer/?search=25', content_type='application/json')
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data[0]['gubn'], self.sewer1['gubn'])
        self.assertEqual(response.status_code, 200)


    """
    필수 요소(GUBN) 1개 + 선택 요소(2개)
    uccess Test Case : 25개
    method : GET
    param : gubn, start_index, end_index
    """













