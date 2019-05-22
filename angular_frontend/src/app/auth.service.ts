import { Injectable } from '@angular/core';
import { Http, Response, RequestOptions, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import {TopDonations,DonationComments,LoginUser} from './campaign-model';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class AuthService {

  private url: string = 'http://localhost:8000/rest-auth';

  constructor(private http: Http) { }


  login(user:LoginUser):Observable<LoginUser[]>{
   	 let headers = new Headers({ 'Content-Type': 'application/json' });
     headers.append('X-CSRFToken', this.getCookie('csrftoken'));
 	 let options = new RequestOptions({ headers: headers,withCredentials: true});
    console.log(user+'hell');
    const getLoginUrl = this.url + '/login/';
    return this.http
      .post(getLoginUrl, user, options)
      .map(
      res => {
      console.log(res.status+" yes");
        if (res.status == 200) {

          localStorage.setItem('currentUser', JSON.stringify(res.json().key));
        }
        return res.json();
      },
      err => {
        return err;
      }
      )
  }

  getCookie(name) {
    let value = "; " + document.cookie;
    let parts = value.split("; " + name + "=");
    if (parts.length == 2) 
      return parts.pop().split(";").shift();
  }
 
  logout() {
    localStorage.removeItem('currentUser');
  }


}
