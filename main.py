# 기존 데이터  - 2020년 1월~6월까지 6개월간의 관측된 데이터를 활용

# 2020 설 연휴 기간(1월 24일 부터 27일)
# 2020 추석 기간 제외(9/30 ~ 10/04)
# 2021 설 연휴 제외(2/11 ~ 14)

# 환자현황 변수는 COVID-19 확진, 검사, 사망, 격 리 등 유사 정보를 파생해 만든 변수를 포함하고 있 으므로 독립변수 간
# 강한 상관관계로 다중공선성 (multicollinearity) 문제가 발생할 수 있다. 다중공선 성 문제는 모형 신뢰도와 안정성을 해칠
# 우려가 있어 분산팽창인자(variance inflation factor; VIF)를 이 용해 정보 중복이 가장 심한 변수부터 순차적으로 모형에서 제거해 최종 독립변수를 선정했다

# 회귀모형의 유의성 검정 결과를 통해 모형 의 유의성을 판단했고, 적합성은 결정계수와 수정 결정계수에 기반해 판단했다. 끝으로 잔차 분석을 통해 모형 가정을 검토
# 먼저, COVID-19 환자현황 변수 중 격리 해제율(%), 현재 격리자 증감률(%), 누적 검사자 증감률(%),
# 신규 확 진자 수 4개 변수가 교통량에 통계학적으로 유의미 한 영향을 미쳤다. COVID-19 환자현황 변수는 모두 기준일자 기준 전일(lag 1)을 적용


# a) 가장 유의한 변수는 격리 해제율로 격리 해제 율이 높아질수록 교통량이 증가하는 양(+)의 관계
# (c) 누적 검사자 증감률 역시 유의한 영향을 나타 냈다. 누적 검사자 증감률은 검사자 수의 증감추세 를 나타내는 변수로,
# 양수인 경우 증가 추세에, 음수 인 경우 감소 추세에 있음을 의미한다. 누적 검사자 증감률이 증가할수록 교통량은 감소하는 부(-)의 관 계를
# (d) 신규 확진자 수가 증가함에 따라 교통량이 감 소하는 부(-)의 관계
# 신규 확진자 수가 1명 증가할 때 교통량은 평균 886대 감소했다. 영향도 측면에서 유의한 COVID-19 환자현황 변수 중 두 번째로 높은 영향력 을 나타냈다

# 시계열 데이터를 이용한 회귀 모형은 잔차의 독립성 을 확인하는 것이 중요하다. 잔차의 독립성은 잔차 에 대한 ACF, PACF 그래프를 통해 확인했고, 그 결 과 독립성 가정을 만족

# 관계된 변수들을 제거하고 회귀분석을 한것과 안한 것을 비교한다
# 상관계수를 구해본다
# COVID-19가 이동성에 미치는 영향요인 분석

# 516일 데이터 수집

import dataframe_image as dfi
import pandas as pd
import statsmodels.graphics.tsaplots as sgt
from matplotlib import pyplot as plt


def descriptive_statistics():
    hangul_mapper = {
        "sm_tp1_t": "1종교통량(합계)",
        "sm_tp2_t": "2종교통량(합계)",
        "sm_tp3_t": "3종교통량(합계)",
        "sm_tp4_t": "4종교통량(합계)",
        "sm_tp5_t": "5종교통량(합계)",
        "sm_tp6_t": "6종교통량(합계)",
        "sm_tot_t": "교통량(합계)",
        "confirmed": "누적확진자",
        "death": "누적사망자",
        "released": "누적격리해제",
        "tested": "누적검사자",
        "negative": "누적음성",
        "critical": "누적위중증",
        "i_quarant": "현재격리자수",
        "i_under_test": "현재검사자수",
        "i_nw_confirm": "신규확진자수",
        "i_nw_quarant": "신규격리자수",
        "i_nw_release": "신규격리해제자수",
        "i_nw_test": "신규검사자수",
        "i_nw_death": "신규사망자수",
        "i_confirm_id_rto": "확진자증감률",
        "i_quarant_id_rto": "현재격리자증감률",
        "i_test_id_rto": "누적검사증감률",
        "i_test_cnfm_rto": "검사자확진율",
        "i_confirm_rto": "확진율",
        "i_fatality_rto": "치명률",
        "i_release_rto": "격리해제율",
        "i_critical_rto": "위중증증감률",
        "i_critical": "위중증환자수"
    }
    data = pd.read_csv('./rawdata/totally_raw_data_delete_expression.csv')
    statistic_data = []
    col = ["한글 변수명", "영문 변수명", "N", "평균", "표준편차", "최솟값", "최댓값"]
    for key in data.keys():
        if key == 'date':
            continue
        statistic_data.append([
            hangul_mapper.get(key),
            key,
            data[key].__len__(),
            round(data[key].mean(), 2),
            round(data[key].std(), 2),
            round(data[key].min(), 2),
            round(data[key].max(), 2)])

    statistic_df = pd.DataFrame(statistic_data, columns=col)
    # 주석 해제 시 이미지 생성
    dfi.export(statistic_df, 'image/statistic_view.png')
    return data


def calc_vif():
    # https://mindscale.kr/course/basic-stat-python/13/
    pass


def calc_correlation():
    # https://mindscale.kr/course/basic-stat-python/6/
    pass


def regression_analysis():
    pass


if __name__ == '__main__':
    data = descriptive_statistics()
