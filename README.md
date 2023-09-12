# Backjoon
### 2023-09-12 Backjoon 1043 거짓말
1. 문제 내용

	Known_list와 Party list를 중복 없이 합치는 문제
	파티의 순서가 정해지지 않아 완전탐색으로 Known_list를 update한 후
	이후에 count를 늘려가며 result를 제출

2. 틀린점

	1. 파티의 순서를 임의로 설정하여 Known_list를 update 함
	2. Union을 사용하지 않고 + 만 사용해서 set을 합침
	3. Debuging 실수

3. 최종 결과

	문제 해결(2023-09-12)


### 2023-09-12 Backjoon 5186 파티를 열어라
1. 문제 내용
	
	Drunk people와 Not Drunk people를 나눠 차량에 최대한 많이 태우는 문제
	Not Drunk people를 먼저 넣고 이후 Drunk people에 대한 처리한 후
	남은 인원수를 계산

2. 틀린점
	
	1. Drunk people와 Not Drunk people를 구분하고 각 차량에 배치까지 성공
	But, iter 과정에서 생기는 문제를 체크하지 못함

3. 최종결과
	
	문제 미해결 (2023-09-12)

