import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs/Subject';

@Injectable({
  providedIn: 'root'
})
export class MapsService {

  public lat: number = 43.678418;
  public lng: number = -79.809007;
  public zoom: number = 8;

  public newCoordinators = new Subject();

  public openWindow = new Subject();

  constructor(  ) { }

  // getLocation() {
  //   return this.http.get<Location>('http://api.ipapi.com/api/chec')
  // }
}
