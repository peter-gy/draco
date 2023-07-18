import { TopLevelUnitSpec } from 'vega-lite/build/src/spec/unit';
import { Field } from 'vega-lite/build/src/channeldef';
/**
 * Convert from ASP to Vega-Lite.
 */
export default function asp2vl(facts: string[], url?: string): TopLevelUnitSpec<Field>;
