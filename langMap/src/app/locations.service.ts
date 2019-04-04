import { Injectable } from '@angular/core';
import { Marker } from '../models';

@Injectable()
export class LocationsService {

  // @Todo: replace markers by an API
  markers: Marker[] = [    
    {
      lat: -27.153911568227922,
      lng: -109.37454808682332,
      title: 'Rapa Nui',
      icon: 'https://www.ftsgps.com/wp-content/uploads/2017/05/icon-location-100.png',
      draggable: false,
      street: '',
      city: 'Hanga Roa',
      state: 'Rapa Nui (Easter Island)',
      postalcode: '',
      email: '',
      phone: '',
      website: 'http://example.com',
      detail: 'InfoWindow content'
    }
  ];

  
  constructor() { }

  getMarkers() {
    return this.markers;
  }

}