File "knapsackDev_BruteForce.py" is a knapsack packing algorithm taking a brute force approach. This file is a re-written assignment from my MS in Business Analytics degree from William & Mary. It runs a heuristic algorithm to efficiently pack "knapsacks" with items of varying volumes and maximize the total value.


File "knapsack.json" is a JSON file containing the knapsack problems. This file contains 10 knapsack problems (as dictionaries, stored in a list). Here is the full contents of this file, reformatted for readability.


[

{"cap": 4.0, "opt": 14.0, "source": "Initial debugging data", 
"data": [[1.0, 1.0], [1.0, 2.0], [1.0, 3.0], [1.0, 4.0], [1.0, 5.0]]}, 

{"cap": 17.0, "opt": 41.0, "source": "Trick problem where a low-value denisty item is optimal to include in knapsack", 
"data": [[2.0, 5.0], [2.0, 5.0], [2.0, 5.0], [2.0, 5.0], [2.0, 5.0], [2.0, 5.0], [2.0, 5.0], [2.0, 5.0], [3.0, 6.0]]}, 

{"cap": 165.0, "opt": 309.0, "source": "p01 from http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html", 
"data": [[23.0, 92.0], [31.0, 57.0], [29.0, 49.0], [44.0, 68.0], [53.0, 60.0], [38.0, 43.0], [63.0, 67.0], [85.0, 84.0], [89.0, 87.0], [82.0, 72.0]]}, 

{"cap": 26.0, "opt": 51.0, "source": "p02 from http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html", 
"data": [[12.0, 24.0], [7.0, 13.0], [11.0, 23.0], [8.0, 15.0], [9.0, 16.0]]}, 

{"cap": 190.0, "opt": 150.0, "source": "p03 from http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html", 
"data": [[56.0, 50.0], [59.0, 50.0], [80.0, 64.0], [64.0, 46.0], [75.0, 50.0], [17.0, 5.0]]}, 

{"cap": 50.0, "opt": 107.0, "source": "p04 from http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html", 
"data": [[31.0, 70.0], [10.0, 20.0], [20.0, 39.0], [19.0, 37.0], [4.0, 7.0], [3.0, 5.0], [6.0, 10.0]]}, 

{"cap": 104.0, "opt": 900.0, "source": "p05 from http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html", 
"data": [[25.0, 350.0], [35.0, 400.0], [45.0, 450.0], [5.0, 20.0], [25.0, 70.0], [3.0, 8.0], [2.0, 5.0], [2.0, 5.0]]}, 

{"cap": 170.0, "opt": 1735.0, "source": "p06 from http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html", 
"data": [[41.0, 442.0], [50.0, 525.0], [49.0, 511.0], [59.0, 593.0], [55.0, 546.0], [57.0, 564.0], [60.0, 617.0]]}, 

{"cap": 750.0, "opt": 1458.0, "source": "p07 from http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html", 
"data": [[70.0, 135.0], [73.0, 139.0], [77.0, 149.0], [80.0, 150.0], [82.0, 156.0], [87.0, 163.0], [90.0, 173.0], [94.0, 184.0], [98.0, 192.0], [106.0, 201.0], [110.0, 210.0], [113.0, 214.0], [115.0, 221.0], [118.0, 229.0], [120.0, 240.0]]}, 

{"cap": 6404180.0, "opt": 13549094.0, "source": "p08 from http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html", 
"data": [[382745.0, 825594.0], [799601.0, 1677009.0], [909247.0, 1676628.0], [729069.0, 1523970.0], [467902.0, 943972.0], [44328.0, 97426.0], [34610.0, 69666.0], [698150.0, 1296457.0], [823460.0, 1679693.0], [903959.0, 1902996.0], [853665.0, 1844992.0], [551830.0, 1049289.0], [610856.0, 1252836.0], [670702.0, 1319836.0], [488960.0, 953277.0], [951111.0, 2067538.0], [323046.0, 675367.0], [446298.0, 853655.0], [931161.0, 1826027.0], [31385.0, 65731.0], [496951.0, 901489.0], [264724.0, 577243.0], [224916.0, 466257.0], [169684.0, 369261.0]]}

]



