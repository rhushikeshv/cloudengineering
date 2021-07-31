import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PartService {

  constructor(private http: HttpClient) { }

  getParts(): Observable<any>{
    return this.http.get('https://1dqe2dt924.execute-api.us-east-1.amazonaws.com/parts');
  }
}
