import styles, { layout } from "../style";
import Button from "./Button";


const Explanation = () => (
  <section id = "product" className={layout.section}>
    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
       Pre-Detect unusual behaviour <br className="sm:block hidden" /> in few easy
        steps.
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        -Red: Weapons and violent objects <br></br>
        -Yellow: Unusual behaviour and violent actions<br></br>
        -Green: Normal and safe
      </p>

      {/* <Button styles={`mt-10`} /> */}
    </div>
  </section>
);

export default Explanation;