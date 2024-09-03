'''
Print the area of a given polygon. The polygon consists of N vertices (x1, y1), (x2, y2), …, (xN, yN). The vertices (xi, yi) and (xi+1, yi+1) are adjacent for i = 1, 2, …, N−1, and the vertices (x1, y1) and (xN, yN) are also adjacent.


Input Format

The first line of input has an integer N: the number of vertices. Next N lines describe the vertices. The ith such line has two integers xi and yi separated by space. You may assume that the polygon is simple, i.e., it does not intersect itself.

Output Format

Print the area of the Polygon.


Constraints

3 ≤ N ≤ 1000

-103 ≤ xi, yi ≤ 103


Example

Input

4

1 1

4 2

3 5

1 4


Output

16


Explanation

Self Explanatory
'''

n = int(input())

vertices = []

for _ in range(n):
  x, y = map(int, input().split())
  vertices.append((x, y))

area = 0
for i in range(n):
  x1, y1 = vertices[i]
  x2, y2 = vertices[(i+1) % n]
  area += (x1*y2 - x2*y1)

area = abs(area)
print(int(area))