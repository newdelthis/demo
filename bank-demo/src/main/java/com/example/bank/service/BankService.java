
package com.example.bank.service;
import java.util.*; import org.springframework.stereotype.Service; import com.example.bank.model.Account;
@Service
public class BankService{
private final Map<Integer,Account> accounts=new HashMap<>(); private int nextId=1;
public List<Account> all(){return new ArrayList<>(accounts.values());}
public Account get(int id){return accounts.get(id);}
public Account create(Account a){a.setId(nextId++);accounts.put(a.getId(),a);return a;}
public Account deposit(int id,double amt){Account a=accounts.get(id);if(a!=null)a.setBalance(a.getBalance()+amt);return a;}
public Account withdraw(int id,double amt){Account a=accounts.get(id);if(a!=null)a.setBalance(a.getBalance()-amt);return a;}
public void delete(int id){accounts.remove(id);}
}
