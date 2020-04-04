---
layout: post
title:  JAVA 基础知识
date:   2019-03-23
categories: JAVA
---

<!-- MarkdownTOC -->


> 本文为此网站学习笔记,仅作个人学习记录之用


1. 多态

```java
public class HelloWorld{
    public static void main(String[] args) {
        // 给一个有普通收入、工资收入和享受国务院特殊津贴的小伙伴算税:
        //define a class array
        Income[] incomes = new Income[] {
                new Income(3000),
                new Salary(7500)
        };
        System.out.println(totalTax(incomes));
    }

    public static double totalTax(Income... incomes) {
        double total = 0;
        for (Income income: incomes) {
            total = total + income.getTax();
        }
        return total;
    }
}

class Income {
    protected double income;

    public Income(double income) {
        this.income = income;
    }

    public double getTax() {
        return income * 0.1; // 税率10%
    }
}

class Salary extends Income {
    public Salary(double income) {
        super(income);
    }

    @Override
    public double getTax() {
        if (income <= 5000) {
            return 0;
        }
        return (income - 5000) * 0.2;
    }
}

```

> 子类与父类有相同的方法getTax(),调用子类Income时直接用子类覆盖的方法,

> @Override和@Overload不同的是，如果方法签名如果不同，就是@Overload，@Overload方法是一个新方法；如果方法签名相同，并且返回值也相同，就是@Override。

用数组实现类集合：

> Income[] incomes = new Income[] { new Income(3000), new SalaryIncome(7500), new RoyaltyIncome(12000) };

2. 抽象类&接口

当父类方法可以省略，完全由子类实现，可以将父类定义为抽象类，作为一种规范

在Java中，一个类只能继承自另一个类，不能从多个类继承。但是，一个类可以实现多个interface

因为interface是一个纯抽象类，所以它不能定义实例字段。但是，interface是可以有静态字段的，并且静态字段必须为final类型：
> public static final int FEMALE = 2;

实际上，因为interface的字段只能是public static final类型，所以我们可以把这些修饰符都去掉
> int FEMALE = 2;

3. 等于

两个字符串比较，必须总是使用equals()方法。
要忽略大小写比较，使用equalsIgnoreCase()方法。