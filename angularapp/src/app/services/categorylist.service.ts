import { Injectable } from '@angular/core';
import {BaseService} from './base.service';
import {Category} from './../models/category';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import {Observable} from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable()
export class CategorylistService extends BaseService{

  private url = "categories/";

  constructor(private http:HttpClient) {
    super();
  }

  public getCategoryDetails(id):Observable<Category>{
    return this.http.get<Category>(this.API_BASE_URL+this.url+id+"/");
  }

  public getCategoryList():Observable<Category[]>{

      return this.http.get<Category[]>(this.API_BASE_URL+this.url)
        .pipe(
          tap(categories => this.log(`fetched categories`)),
          catchError(this.handleError('getCategories', []))
        );
  }
}
