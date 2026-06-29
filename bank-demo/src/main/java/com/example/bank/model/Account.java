
package com.example.bank.model;
public class Account{
private Integer id; private String name; private double balance;
public Account(){}
public Account(Integer id,String name,double balance){this.id=id;this.name=name;this.balance=balance;}
public Integer getId(){return id;} public void setId(Integer id){this.id=id;}
public String getName(){return name;} public void setName(String name){this.name=name;}
public double getBalance(){return balance;} public void setBalance(double balance){this.balance=balance;}
}
