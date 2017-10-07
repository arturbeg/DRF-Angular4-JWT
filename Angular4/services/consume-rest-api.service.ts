import {Injectable} from '@angular/core';
import {Http, Response, Headers, RequestOptions} from "@angular/http";
import {Observable} from 'rxjs/Rx';
import 'rxjs/add/operator/map'

@Injectable()
export class ConsumeRestAPIServices {
	 public token:any;
    constructor(private http:Http) {
     var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        this.token = currentUser && currentUser.token;
    }

    create(value:any) {
        # Creating new database for orderbook
        var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        var token = currentUser.token;
        #common header for all the API request made
        let headers = new Headers({'Content-Type': 'application/json','Accept': 'application/json',});
        headers.append('Authorization','JWT'+' '+token);
        let options = new RequestOptions({headers: headers});
        return this.http.post('http://127.0.0.1:8000/api/data/create/', value, options).map((res:Response) => res.json());
    }
    login(username:any, password: any) {
    #Just Jwt based login session 
     let headers = new Headers({'Content-Type': 'application/json','Accept': 'application/json',});
        let options = new RequestOptions({headers: headers});
        return this.http.post('http://127.0.0.1:8000/api/data/api-token-auth/',({username,password }),options)
            .map((response: Response) => {
                let token = response.json() && response.json().token;
                if (token) {
                    this.token = token;
                    localStorage.setItem('currentUser', JSON.stringify({ username: username, token: token }));
                    return token;
                } else {
                    return false;
                }
            });
    }
      getValue(){
      # Retrive the orderbook database for login user
      var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        var token = currentUser.token;
        let headers = new Headers({'Content-Type': 'application/json','Accept': 'application/json'});
        headers.append('Authorization','JWT'+' '+token);
        let options = new RequestOptions({headers: headers});
        return this.http.get('http://127.0.0.1:8000/api/data/',options).map((res:Response) => res.json());
    }

        putValue(symbol:any, price:any){
        # Edit the database for specific user
        var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        var token = currentUser.token;
        let headers = new Headers({'Content-Type': 'application/json','Accept': 'application/json'});
        headers.append('Authorization','JWT'+' '+token);
        let options = new RequestOptions({headers: headers});
        return this.http.put('http://127.0.0.1:8000/api/data/145/edit/',({symbol,price}),options).map((res:Response) => res.json());
    }

       justgetValue(){
        # Retrive the database for pre-filling the edit form 
        var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        var token = currentUser.token;
        let headers = new Headers({'Content-Type': 'application/json','Accept': 'application/json'});
        headers.append('Authorization','JWT'+' '+token);
        let options = new RequestOptions({headers: headers});
        return this.http.get('http://127.0.0.1:8000/api/data/145/edit/',options).map((res:Response) => res.json());
    }

 }