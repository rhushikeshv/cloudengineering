import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class EcrService {

  constructor(private http: HttpClient) { }

  getEcrs():Observable<any>{
    return this.http.get('https://gzpbuhtrnj.execute-api.us-east-1.amazonaws.com/ecrs')
  }
}
