# 代码生成时间: 2025-10-30 13:58:16
import scrapy
def __init__(self):
    """初始化供应链管理系统"""
    self.supplies = {}
def add_supply(self, name, quantity):
    """添加供应链中的物资
    :param name: 物资名称
    :param quantity: 物资数量
    """
    if name in self.supplies:
        self.supplies[name] += quantity
    else:
        self.supplies[name] = quantity
    print(f"Added {quantity} {name} to the supply chain.")

    return self.supplies

def remove_supply(self, name, quantity):
    """从供应链中移除物资
    :param name: 物资名称
    :param quantity: 要移除的物资数量
    """
    if name not in self.supplies:
        raise ValueError(f"{name} is not in the supply chain.")
    elif self.supplies[name] < quantity:
        raise ValueError(f"Not enough {name} to remove.")
    else:
        self.supplies[name] -= quantity
        print(f"Removed {quantity} {name} from the supply chain.")

    return self.supplies

def get_supply(self, name):
    """获取供应链中物资的数量
    :param name: 物资名称
    """
    return self.supplies.get(name, 0)

def get_total_supply(self):
    """获取供应链中所有物资的总数量
    """
    return sum(self.supplies.values())

def update_supply(self, name, quantity):
    """更新供应链中物资的数量
    :param name: 物资名称
    :param quantity: 新的物资数量
    """
    if name not in self.supplies:
        raise ValueError(f"{name} is not in the supply chain.")
    self.supplies[name] = quantity
    print(f"Updated {name} quantity to {quantity}.")
    return self.supplies

# 示例使用
if __name__ == "__main__":
    scm = SupplyChainManagement()
    scm.add_supply("Steel", 100)
    scm.add_supply("Copper", 50)
    print(scm.get_supply("Steel"))
    scm.remove_supply("Steel", 20)
    print(scm.get_supply("Steel"))
    scm.update_supply("Copper", 75)
    print(scm.get_total_supply())
