# Component - Bootstrap Callout

Component for rendering a callout message like the ones found in the Bootstrap documentation.

![x][render_preview]

## Usage

```
import { callout, ICalloutData } from 'components';


const calloutData = {
  type: 'warning',  // If unspecified, will default to 'primary'
  title: 'Getting Started',
  content: m('p', ['Some text']),
};
m(callout, { calloutData });
```


## Interfaces

```
export interface ICalloutData {
  type?: string;
  title: string;
  content: Mithril.Vnode<any, any>;
}
```

[render_preview]: bs-callout.png
