import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MapsService {

  constructor(private http: HttpClient) { }

  // getLocation() {
  //   return this.http.get<Location>('http://api.ipapi.com/api/chec')
  // }
}
