## Question
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

#### Example
> scores = [12, 24, 10, 24]

Scores are in the same order as the games played. She tabulates her results as follows:

                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1
Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

#### Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

- int scores[n]: points scored per game
#### Returns

- int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
#### Input Format

The first line contains an integer n, the number of games.
The second line contains n space-separated integers describing the respective values of score(0), score(1), ... score(n-1).

#### Constraints

- 1 < n <= 1000
- 0 <= scores[i] <= 10^8

_____


## 풀이


농구 점수가 정수 리스트로 주어질 때, 최고 기록과 최저 기록이 갱신되는 횟수를 return하는 문제다. 

1. 먼저 나는 result에 갱신 횟수를 담기위해 [0,0]배열로 선언해주었다.
2. scores를 돌면서 최저기록 혹은 최고기록이 갱신되는지 확인하며 갱신되었다면 result의 해당 인덱스에 +1 해준다. 
3. 갱신되었을 때, 기록도 갱신된 기록으로 바꿔준다.
4. result를 return한다.
