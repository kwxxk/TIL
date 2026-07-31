def sum_pos_num():
    current_sum = 0
    results = []
    while True:
        num = int(input())

        if num == 0:    #우선 순위 1 print후 break
            if current_sum > 0:
                results.append(current_sum)
            break

        if num < 0:     #
            if current_sum > 0:
                results.append(current_sum)
                current_sum = 0

        else:
                current_sum += num
    for result in results:
         print(result)

    return results

sum_pos_num()