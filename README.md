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
