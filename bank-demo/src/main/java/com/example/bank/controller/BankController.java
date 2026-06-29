
package com.example.bank.controller;
import org.springframework.web.bind.annotation.*; import java.util.*; import com.example.bank.model.Account; import com.example.bank.service.BankService;
@RestController
@RequestMapping("/accounts")
public class BankController{
private final BankService service;
public BankController(BankService s){this.service=s;}
@GetMapping public List<Account> all(){return service.all();}
@GetMapping("/{id}") public Account get(@PathVariable int id){return service.get(id);}
@PostMapping public Account create(@RequestBody Account a){return service.create(a);}
@PostMapping("/{id}/deposit") public Account dep(@PathVariable int id,@RequestParam double amount){return service.deposit(id,amount);}
@PostMapping("/{id}/withdraw") public Account wd(@PathVariable int id,@RequestParam double amount){return service.withdraw(id,amount);}
@DeleteMapping("/{id}") public void del(@PathVariable int id){service.delete(id);}
}
