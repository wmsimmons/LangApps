/// <reference types="@types/googlemaps" />
import { Component } from '@angular/core';
import { MapsService } from './maps.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'papahana';

  constructor(private map: MapsService) {}
}

