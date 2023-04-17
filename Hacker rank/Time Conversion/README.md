## Question
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#### Example
> s = '12:01:00PM'

Return `'12:01:00'`

> s = '12:01:00AM'

Return `'00:01:00'`

#### Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

- string s: a time in  hour format
#### Returns

- string: the time in  hour format
#### Input Format

A single string  that represents a time in -hour clock format (i.e.:hh:mm:ssAM  or hh:mm:ssPM ).

#### Constraints

- All input times are valid
#### Sample Input

> 07:05:45PM

#### Sample Output

> 19:05:45



## 풀이

12-hour format으로 입력된 시간을 24-hour format으로 바꿔주는 문제다.
나는 먼저
1. AM과 PM을 c라는 변수에 저장하고
2. 시간만 중요하기 때문에 시간과 그 외로 분리하여 h, e에 각각 저장하였다.
3. c가 PM이면 시간이 12 미만일때만 시간에 12를 더하고
4. c가 AM이면 시간이 12일때만 0으로 바꾸고 나머지는 그대로 둔다.
5. 시간과 나머지를 붙여준다.
6. 만약 완성된 답의 길이가 8보다 작다면 시간이 1의 자리 숫자라는 뜻이다. 따라서 앞에 0을 붙여준다.



