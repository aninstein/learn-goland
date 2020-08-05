#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import numpy as np


def bag_0and1(data):
    """
    01背包问题
    问题描述：有n件物品和容量为m的背包 给出i件物品的重量以及价值 求解让装入背包的物品重量不超过背包容量 且价值最大 。
    特点:这是最简单的背包问题，特点是每个物品只有一件供你选择放还是不放。
    :param data:
    :return:
    """
    print(data)
    total_weight = data.get("total_weight")
    items = data.get("items")
    number = data.get("things_num")
    max_value = _two_dim_function(items, number, total_weight)
    print(max_value)
    pass


def _one_dim_function(data, number, total_weight):
    """
    状态转移方程：
    i：表示第几个物品
    k：表示重量几许
    dp[k] = max(value[i]+dp[k-weight[i]], dp[k])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    total_val = np.array([0] * col)
    for i in range(1, row):
        if i == len(data):
            break
        item = data[i]
        # 这个地方需要是从后面到前面，因为如果从前面到后面的话，会把低层级的j给覆盖掉，
        # https://www.cnblogs.com/kkbill/p/12081172.html
        # 其实是由于状态转移方程为：dp[k](新值) = max(value[i]+dp[k-weight[i]](旧值), dp[k](旧值))
        # 这个k-weight[i]，如果从前往后数的话，这个值就会被上个值更新为新的值而出现错误
        for j in range(col-1, -1, -1):
            value = item.get("value")
            weight = item.get("weight")
            if weight <= j:
                input_val = total_val[j - weight] + value
                total_val[j] = max(input_val, total_val[j])
    return total_val[total_weight - 1]


def _two_dim_function(data, number, total_weight):
    """
    状态转移方程
    i: 表示第几个物品
    j: 表示背包重量
    dp[i][j] = max(value[i]+dp[i-1][j-weight[i]], dp[i-1][j])
    :param data:
    :param number:
    :param total_weight:
    :return:
    """
    # 由于数据从1开始计算因此+1
    row = number + 1
    col = total_weight + 1
    total_val = np.array([0] * (row * col)).reshape(row, col)
    for i in range(1, row):
        if i == len(data):
            break
        item = data[i]
        for j in range(1, col):
            value = item.get("value")
            weight = item.get("weight")
            if weight > j:
                total_val[i][j] = total_val[i-1][j]
            else:
                input_val = total_val[i-1][j-weight] + value
                noput_val = total_val[i-1][j]
                total_val[i][j] = max(input_val, noput_val)
    return total_val[number-1][total_weight]


def bag_complete(data):
    """
    完全背包问题
    问题描述：有n件物品和容量为m的背包 给出i件物品的重量以及价值 求解让装入背包的物品重量不超过背包容量 且价值最大 。
    特点：题干看似与01一样 但它的特点是每个物品可以无限选用。
    :param data:
    :return:
    """
    pass


def bag_multiple(data):
    """
    多重背包问题
    问题描述：有n件物品和容量为m的背包 给出i件物品的重量以及价值 还有数量 求解让装入背包的物品重量不超过背包容量 且价值最大 。
    特点 ：它与完全背包有类似点 特点是每个物品都有了一定的数量。
    :param data:
    :return:
    """
    pass


def create_random_bag_data(things_num, bag_type="01", is_random=True):
    if not is_random:
        return {}

    items = []
    for i in range(things_num):
        if bag_type == "multiple":
            number = random.randint(1, 50)
        elif bag_type == "complete":
            number = 999999
        else:
            number = 1
        items.append({
            "number": number,
            "weight": random.randint(1, 100),
            "value": random.randint(1, 1000)
        })
    total_weight = random.randint(150, 350)
    return {
        "items": items,
        "total_weight": total_weight,
        "things_num": things_num
    }


if __name__ == '__main__':
    things_number = 10
    data = create_random_bag_data(things_number, bag_type="01")
    print("bag_0and1 >>>>>>>>>>>>")
    bag_0and1(data)

    print("bag_complete >>>>>>>>>>>>")
    data = create_random_bag_data(things_number, bag_type="complete")
    bag_complete(data)

    print("bag_multiple >>>>>>>>>>>>")
    data = create_random_bag_data(things_number, bag_type="multiple")
    bag_multiple(data)
