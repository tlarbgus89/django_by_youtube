# -*- coding: utf-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "recon0928",
    database = "testdb",
)
# Create Cursor Instance
my_cursor = mydb.cursor()

a = "관세등부과처분취소"
b = "[대법원 2019. 1. 17., 선고, 2016두45813, 판결]"
c = '''【판시사항】
아시아·태평양 무역협정 원산지 확인 기준 등에 관한 규칙 제8조 제3항에서 정한 증빙서류를 제출하기 어려운 사정이 있는 경우, 다른 신빙성 있는 자료로 대체할 수 있는지 여부(적극) 및 위 조항 제1호에서 정한 ‘수출참가국에서 발행된 통과 선하증권’이 제출되지 않았다는 이유만으로 ‘아시아·태평양 경제사회위원회의 개발도상회원국 간 무역협정에 관한 1차 협정(방콕협정)에 대한 개정으로서 아시아·태평양 무역협정’의 직접운송의 요건을 충족하지 못한다고 단정하여 위 협정에 따른 협정세율 적용을 부인할 수 있는지 여부(소극)
     '''
d = '''【판결요지】
아시아·태평양 무역협정 원산지 확인 기준 등에 관한 규칙 제8조 제3항의 문언, 체계, 제정 경위, ‘아시아·태평양 경제사회위원회의 개발도상회원국 간 무역협정에 관한 1차 협정(방콕협정)에 대한 개정으로서 아시아·태평양 무역협정’(이하 ‘아태무역협정’이라 한다)과 그 부속서를 비롯한 관련 법령의 직접운송에 관한 규정들의 취지와 목적 등을 모두 종합할 때, 위 조항은 아태무역협정 부속서에서 정한 직접운송 규정을 원활히 실시·집행하기 위하여 관세당국에 제출할 증명서류에 관하여 일반적으로 신빙성을 높게 보는 대표적인 증빙서류들을 정하고 있는 것으로서, 이를 제출하기 어려운 사정이 있는 경우에는 다른 신빙성 있는 자료로 대체할 수 있다. 따라서 제1호의 ‘수출참가국에서 발행된 통과 선하증권’을 발급받기 어려운 사정이 있는 경우에는 같은 항 제4호에 따라 다른 신빙성 있는 증명서류를 제출하여 직접운송 간주 요건의 충족을 증명할 수 있고, 단지 위 ‘통과 선하증권’이 제출되지 않았다는 형식적인 이유만으로 아태무역협정의 직접운송의 요건을 충족하지 못한다고 단정하여 협정세율 적용을 부인할 수는 없다.
     '''
e = '''【참조조문】
아시아·태평양 경제사회위원회의 개발도상회원국 간 무역협정에 관한 1차 협정(방콕협정)에 대한 개정으로서 아시아·태평양 무역협정 제8조, 아시아·태평양 무역협정 원산지 확인 기준 등에 관한 규칙 제8조 제3항, 아시아·태평양 무역협정의 부속서 II(아시아·태평양 무역협정 원산지 규정) 제1조, 제5조, 아시아·태평양 무역협정에 의한 물품의 원산지 증명 및 검증 운영절차 제9조, 구 관세법(2014. 1. 1. 법률 제12159호로 개정되기 전의 것) 제229조 제3항


【전문】
【원고, 상고인】
주식회사 영원무역 (소송대리인 법무법인 세종 담당변호사 김형수 외 1인)

【피고, 피상고인】
서울세관장

【원심판결】
서울고법 2016. 6. 28. 선고 2016누30356 판결

【주 문】
원심판결을 파기하고, 사건을 서울고등법원에 환송한다.


【이 유】
상고이유를 판단한다. 
1.  사안의 개요와 쟁점 
가.  사안의 개요와 소송 경과
(1) 원고는 2011. 10. 17. 및 2012. 3. 8. 중국에서 생산된 신발 등(이하 ‘이 사건 물품’이라고 한다)을 홍콩을 경유하여 수입하면서「아시아·태평양 경제사회위원회의 개발도상회원국 간 무역협정에 관한 1차 협정(방콕협정)에 대한 개정으로서 아시아·태평양 무역협정」(이하 ‘아태무역협정’이라고 한다)에 따른 협정세율을 적용하여 수입신고를 하고 관세와 부가가치세를 납부하였다.
(2) 피고는 기획재정부령인 아시아·태평양 무역협정 원산지 확인 기준 등에 관한 규칙(이하 ‘이 사건 규칙’이라고 한다) 제8조 제3항 제1호의 ‘수출참가국에서 발행된 통과 선하증권’이 제출되지 않았다는 등의 이유로, 2013. 7. 31. 및 2013. 9. 9. 협정세율 적용을 부인하여 원고에게 관세와 부가가치세를 경정·고지하였고, 이후 원고의 심판청구에 따라 개시된 조세심판 과정에서 각 가산세 부분이 취소되었다(남은 부분을 ‘이 사건 처분’이라고 한다).
(3) 원심은, 아태무역협정에 따른 협정세율을 적용받기 위해서는 ‘통과 선하증권’이 반드시 제출되어야 한다고 본 피고의 이 사건 처분이 적법하다고 판단하였다. 이 사건 규칙은 구 관세법(2014. 1. 1. 법률 제12159호로 개정되기 전의 것) 제229조 제3항의 위임에 따른 것으로서 법규적 효력이 있고, ‘모두 제출되어야 한다’라는 그 문언상 필수서류로 볼 수밖에 없다는 것이다. 원고가 이에 불복하여 상고하였는데, 아태무역협정과 그 부속서에 명시적 근거 없이 이 사건 규칙의 일부 문언만으로 ‘통과 선하증권’을 협정 적용을 위한 필수서류로 취급할 수 없으며, 이는 관세 당국의 그동안의 공적 견해표명 내지 비과세관행에도 반한다는 점 등을 상고이유로 하였다.
 
나.  쟁점
이 사건의 주된 쟁점은 이 사건 규칙 제8조 제3항 제1호의 ‘통과 선하증권’이 제출되지 않은 경우에는 아태무역협정에 따른 협정세율의 적용이 일률적으로 배제되는지 여부이다.
 
2.  상고이유 제1점 내지 제3점에 관하여 
가.  관련 법령 규정
2006. 6. 30. 국회 동의를 거쳐 2006. 9. 1. 발효된 아태무역협정의 부속서 II(아태무역협정 원산지 규정) 제1조는 다른 참가국으로부터 일방 참가국의 영역으로 직접 운송된 상품으로서 원산지 요건을 충족하는 경우를 협정에 따른 특혜 양허의 대상으로 정하고 있다. 제5조는 ‘직접운송’이라는 표제 아래 직접운송으로 보는 경우를 ‘상품이 비참가국의 영역을 통과하지 않고 운송되는 경우’(가항) 외에도 ‘환적 또는 일시 보관 여부에 관계없이 하나 또는 그 이상의 비참가 중계국을 경유하여 운송된 상품으로서 다음 각호의 요건을 충족하는 경우’(나항)를 명시하고 있다. 위 나항의 요건은 ‘지리적 이유 또는 전적으로 운송상의 이유로 통과를 위한 반입은 정당화된다’(1호), ‘경유국에서 교역이나 소비되지 않은 상품’(2호), ‘경유국에서 하역, 재선적, 기타 정상의 상태를 유지하기 위해 요구되는 작업 이외의 어떤 작업도 행하지 않은 상품’(3호)으로 규정되어 있다.
아태무역협정은 그 이행을 감독, 조정, 검토하기 위하여 각 참가국의 경제관련 부처의 각료로 구성된 각료회의를 설치하였는데(제23조), 2007. 10. 26. 제2차 각료회의에서 채택되어 2008. 1. 1. 시행된 「아태무역협정에 의한 물품의 원산지 증명 및 검증 운영절차」(이하 ‘이 사건 운영절차’라고 한다)는 제9조에서 ‘직접운송의 증명서류(Supporting Documents of Direct Transportation)’라는 제목으로 위 협정 원산지규정 제5조 나항에 따라 물품이 참가국의 영역 외의 지역을 통해 운송되는 경우 수입참가국의 세관당국에 제출되어야 하는 서류들로서, ‘수출참가국에서 발행된 통과 선하증권’(1호, the through Bill of Lading issued in the exporting Participating State), ‘수출참가국의 발행당국이 발행한 원산지증명서’(2호), ‘해당 물품과 관련된 상업 송품장 원본’(3호), 그리고 ‘아태무역협정 부속서 II의 원산지 규정 제5조 나항을 준수하였음을 증명하는 서류’[4호, supporting documents which prove the compliance with Rule 5(b) of Annex II to APTA]의 4가지를 정하였다.
이 사건 운영절차를 국내법 체계에 수용하기 위해 구 관세법 제229조 제3항에 근거한 기획재정부령으로 2011. 8. 4. 이 사건 규칙이 제정되었다. 위 규칙 제8조는 ‘직접운송의 원칙’이라는 표제 아래 제2항에서 제3국을 경유하여 운송된 물품에 대해 직접운송으로 간주하기 위한 실체적 요건을 규정하는 한편, 제3항에서 “제2항을 적용받으려면 다음 각호의 서류를 모두 제출하여야 한다.”라고 하면서 ‘수출참가국에서 발행된 통과 선하증권’(1호), ‘수출참가국의 발행당국이 발행한 원산지증명서’(2호), ‘해당 물품과 관련된 상업 송품장 원본’(3호), ‘제2항을 준수하였음을 증명하는 보충 서류’(4호)를 들고 있다.
 
나.  해석
(1) 직접운송의 원칙은 무역협정의 수출참가국에서 발송된 물품이 수입참가국에 도착한 물품과 동일함을 확인하고, 특혜관세를 적용받을 수 있는 원산지 물품이 운송과정에서 추가로 가공되거나 특혜관세를 적용받을 수 없는 물품과 뒤바뀌게 될 가능성을 방지하기 위한 것이다. 그리고 무역협정에서 이러한 직접운송의 원칙을 규정할 때에는 일정한 요건하에 비참가국 경유 시에도 직접운송을 간주하는 규정을 함께 두고 있다. 국제물품거래에 따른 운송 시 지리적 이유나 운송상의 편의 등으로 인하여 제3국을 단순 경유하는 경우가 종종 있고, 그러한 물품에 대해서는 협정 참가국 간의 직접운송으로 인정하여 협정세율을 적용하는 것이 무역협정의 원산지 규정 취지에 부합하기 때문이다.
이에 따라 국내 관세법령에서도 같은 취지로 원산지 확인 시 직접운송 간주 규정을 두고 있으며, 실체적 요건 이외에 구체적 증빙서류의 종류 등을 따로 정하고 있지 않다(관세법 제229조, 관세법 시행규칙 제76조, 자유무역협정의 이행을 위한 관세법의 특례에 관한 법률 제7조 제2항 등 참조). 아태무역협정은 위에서 살펴본 바와 같이 부속서 II 제5조 나항에서 물품이 비참가국을 경유하여 운송된 경우에도 직접운송으로 간주될 수 있음을 밝히면서 그 요건으로 위 국내 법령과 마찬가지로 제1호부터 제3호까지 실체적 요건만을 규정하고 있을 뿐이고, 이에 관하여 반드시 어떤 특정한 서류로만 증명하도록 제한하고 있지 않다.
(2) 아태무역협정의 원활한 실시와 집행을 위해 채택된 이 사건 운영절차 제9조와 이를 국내법 체계로 수용한 이 사건 규칙 제8조 제3항에서는 ‘수출참가국에서 발행된 통과 선하증권’(제1호)을 제출하도록 정하고 있다. 그런데 위 운영절차 제9조 제4호에는 ‘아태무역협정 부속서 II의 원산지 규정 제5조 나항을 준수하였음을 증명하는 서류’가 규정되어 있고, 이 사건 규칙 제8조 제3항도 마찬가지로 ‘모두 제출하여야 하는 서류’의 하나로서 ‘제2항을 준수하였음을 증명하는 보충 서류’(제4호)를 들고 있다.
이처럼 마지막에 포괄적인 증명 서류에 관한 문구를 둔 것은 개별적인 물품 운송의 조건과 상황에 맞추어 적합한 증빙자료를 제출할 수 있도록 하기 위함으로 보인다. 증빙서류는 실체적 요건의 구비 여부를 확인하기 위한 신빙성 있는 자료를 가리킨다. 이 사건 규칙 제8조 제3항의 제1호부터 제3호까지 정한 ‘통과 선하증권’, ‘원산지 증명서’, ‘상업 송품장’은 같은 조 제2항의 제1호부터 제3호까지 규정된 직접운송 간주의 실체적 요건, 즉 ‘지리적 이유 또는 전적으로 운송상의 이유로 경유한 것’, ‘경유국에서 관세당국의 통제하에 보세구역에 장치된 것’, ‘경유국에서 하역, 재선적 또는 그 밖의 정상 상태를 유지하기 위하여 요구되는 작업 외의 추가적인 작업을 하지 않은 것’에 하나씩 대응되는 것도 아니다. 결국, 이 사건 규칙 제8조 제3항이 어떠한 경우에도 반드시 제출되어야 하는 필수서류들을 한정적으로 열거하고 있다고 보기는 어렵고, 제1호에 규정된 ‘수출참가국에서 발행된 통과 선하증권’은 관세당국에서 일반적으로 신빙성을 높게 부여하는 운송에 관한 대표적인 증빙서류로서, 이를 제출하기 어려운 특별한 사정이 있는 때에는 다른 신빙성 있는 대체 자료를 제출하여 전적으로 운송상의 이유로 인한 단순 경유 등의 사실을 증명할 수 있다고 봄이 합리적이고 자연스러운 해석이다.
(3) 이 사건 운영절차의 채택 경위, 그 전후로 참가국들의 관련 실무례 등을 살펴보아도, 당시 우리나라와 중국을 비롯한 협정 참가국들 사이에 직접운송의 원칙과 관련하여 단순한 절차상의 운용 규정을 넘어서 아태무역협정에서 정하지 않은 추가적인 법정 필수요건을 창설하고자 하였다고 볼 만한 자료가 없다. 이후 이 사건 규칙의 제정 목적과 경위 등을 살펴보아도 마찬가지이다.
‘통과 선하증권’의 개념 정의나 인정 기준에 관하여 이 사건 운영절차나 이 사건 규칙, 그 밖에 관련 법령 어디에서도 아무런 규정을 두고 있지 않고, 미제출 시 협정세율이 적용되지 않는다는 명시적인 규정이 없는 점은 중요하게 고려되어야 한다. 만일 이를 필요적 서류로 보아 미제출 시에 곧바로 원산지를 인정하지 않고자 하는 취지였다면 협정 참가국들이 이에 관해서 명확한 요건이나 기준을 마련하지 않은 것은 모순으로 보인다. 원산지증명서에 관해서는 아태무역협정과 부속서 등에서 그 요건 등을 상세히 정하고 있을 뿐만 아니라, 원산지증명서가 제출되지 않으면 협정세율을 적용하지 않을 수 있음이 법령에 별도로 명시된 점과 대비된다.
나아가 협정 참가국들의 각 지리적 위치, 무역 현황 및 운송방법의 다양성, 선하증권 등 운송서류의 발급 실무, 컨테이너 번호와 봉인 등에 의한 물품 동일성의 확인 정도, 아태무역협정의 목적과 앞서 본 협정상 원산지 및 직접운송 관련 규정의 취지 등 관련되는 그 밖의 모든 사정에 비추어 보아도, 협정 참가국 간의 물품 운송에 있어 해상운송뿐만 아니라 육로운송이나 항공운송이 전부 또는 일부 구간에서 이루어지는 경우가 적지 않은데, 그러한 경우에도 언제나 전체 운송구간에 대해 한 장의 ‘통과 선하증권’을 발급받아 제출하도록 강제하고 다른 신빙성 있는 증거 방법에 의한 직접운송 간주 요건의 증명 가능성을 원천적으로 배제하려는 취지였다고 보기 어렵다.
이처럼 이 사건 규칙 제8조 제3항이 납세자의 편의와 관세행정의 효율을 고려하여 직접운송 간주 요건 증명을 위한 대표적인 제출서류를 예시적으로 정하는 것은 아태무역협정 부속서의 원산지 규정에서 충분히 예상할 수 있는 직접운송 간주 요건의 실시·집행에 관한 세부 절차적 사항에 속하므로, 전체적인 규범 체계와 관세법 제229조 제3항의 취지에 부합하고 위임 범위의 한계 일탈의 우려도 없다.
(4) 위와 같은 문언, 체계, 제정 경위, 아태무역협정과 그 부속서를 비롯한 관련 법령의 직접운송에 관한 규정들의 취지와 목적 등을 모두 종합할 때, 이 사건 규칙 제8조 제3항은 아태무역협정 부속서에서 정한 직접운송 규정을 원활히 실시·집행하기 위하여 관세당국에 제출할 증명서류에 관하여 일반적으로 신빙성을 높게 보는 대표적인 증빙서류들을 정하고 있는 것으로서, 이를 제출하기 어려운 사정이 있는 경우에는 다른 신빙성 있는 자료로 대체할 수 있다. 따라서 제1호의 ‘수출참가국에서 발행된 통과 선하증권’을 발급받기 어려운 사정이 있는 경우에는 같은 항 제4호에 따라 다른 신빙성 있는 증명서류를 제출하여 직접운송 간주 요건의 충족을 증명할 수 있고, 단지 위 ‘통과 선하증권’이 제출되지 않았다는 형식적인 이유만으로 아태무역협정의 직접운송의 요건을 충족하지 못한다고 단정하여 협정세율 적용을 부인할 수는 없다.
 
다.  이 사건에 대한 적용
따라서 이 사건 물품의 수입신고 시 이 사건 규칙 제8조 제3항 제1호의 ‘통과 선하증권’이 제출되지 않았다고 하더라도, 이러한 사정만으로 곧바로 아태무역협정에 따른 특혜관세가 배제된다고 볼 수 없고, 원심으로서는 이를 제출하기 어려운 사정이 있어서 ‘통과 선하증권’ 이외의 다른 증명서류에 의하여 이 사건 무역협정 부속서Ⅱ 제5조 나항 내지 이 사건 규칙 제8조 제2항의 요건이 충족되었는지를 심리하여 이 사건 처분의 적법 여부를 판단하였어야 할 것이다.
그런데도 원심은 이와 다른 전제에서 그 판시와 같은 이유만으로 이 사건 처분이 적법하다고 단정하고 말았다. 이러한 원심의 판단에는 아태무역협정에서 직접운송으로 간주하기 위한 요건 등에 관한 법리를 오해하여 필요한 심리를 다하지 아니함으로써 판결에 영향을 미친 잘못이 있다. 이를 지적하는 상고이유 주장은 이유 있다.
 
3.  결론
그러므로 나머지 상고이유에 대한 판단을 생략한 채 원심판결을 파기하고, 사건을 다시 심리·판단하게 하기 위하여 원심법원에 환송하기로 하여, 관여 대법관의 일치된 의견으로 주문과 같이 판결한다.


대법관 조희대(재판장) 김재형 민유숙(주심) 이동원
     '''

# Insert Multiple Records

sqlStuff = "INSERT INTO posts_post (title, subtitle, content, content2, content3) VALUES (%s, %s, %s, %s, %s)"
records = [
    (a,b,c,d,e)
]
my_cursor.executemany(sqlStuff, records)
mydb.commit()