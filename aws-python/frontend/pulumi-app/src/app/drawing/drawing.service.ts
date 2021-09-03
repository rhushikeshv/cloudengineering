import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DrawingService {

  constructor(private http: HttpClient) { }

  getDrawings():Observable<any>{
    return this.http.get('https://tr17b1bcib.execute-api.us-east-1.amazonaws.com')
  }
}
