import { Component, OnInit } from '@angular/core';
import { ConsumeRestAPIServices } from '../../services/consume-rest-api.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
 send:Send;
 postStatus:any;
 msg:string;
 username:string;
 password:any;
 value:any;
 value1:any;

  constructor(private ConsumeRestAPIServices:ConsumeRestAPIServices) { 
  }

  ngOnInit() {
  this.ConsumeRestAPIServices.justgetValue().subscribe((value)=>{
  this.value1=value;
   }
   );
  }

  create(symbol,price){
  #Create new database 
  this.msg='Value send';
  this.send=new Send(symbol,price);
  this.ConsumeRestAPIServices.create(this.send).subscribe((status)=>{
  this.postStatus=status;
  }
)
return false;
}

  login(username,password){
  # creating login session using JWT
  this.ConsumeRestAPIServices.login(username,password).subscribe((token)=>{
  this.postStatus=token;
  }
  )
  console.log(this.postStatus);
  if (this.postStatus){
  this.ConsumeRestAPIServices.getValue().subscribe((value)=>{
  this.value=value;
  }
  )
  this.msg=this.postStatus;

  }
  else{
  this.msg='enter correct details';
  }
  return false;
}

putValue(symbol,price){
  this.ConsumeRestAPIServices.putValue(symbol,price).subscribe((value)=>{
  this.value1=value;
  }
)
return false;
}

}

class Send
{
  public symbol:string;
  public price:number;
    constructor(symbol:string,price:number){
        this.symbol=symbol;
        this.price=price;
        }
}

