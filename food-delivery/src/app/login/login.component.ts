import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  logged = false;
  username = '';
  password = '';


  constructor() {}
  login(){
    // this.sharedService.login(this.username,this.password).subscribe(data=>{
    //   this.logged = true;
    // });
    this.logged = true;
    console.log(this.username);
  }

  logout(){
    this.logged = false;
  }

  ngOnInit(): void {
  }
}
